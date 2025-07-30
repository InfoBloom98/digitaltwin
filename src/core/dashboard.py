"""
Web Dashboard for Cybersecurity Simulation
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import threading
import time
from typing import Dict, Any
import json
from datetime import datetime

class Dashboard:
    """Web dashboard for cybersecurity simulation visualization"""
    
    def __init__(self, simulation_engine, config):
        self.simulation = simulation_engine
        self.config = config
        self.app = Flask(__name__)
        CORS(self.app)
        
        # Dashboard state
        self.dashboard_data = {
            'current_time': 0,
            'entity_count': 0,
            'security_score': 0,
            'vulnerabilities': [],
            'attacks': [],
            'anomalies': [],
            'recommendations': [],
            'metrics': {}
        }
        
        # Setup routes
        self._setup_routes()
        
        # Start dashboard in separate thread
        self.dashboard_thread = threading.Thread(target=self._run_dashboard)
        self.dashboard_thread.daemon = True
        self.dashboard_thread.start()
    
    def _setup_routes(self):
        """Setup Flask routes"""
        
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/api/status')
        def get_status():
            return jsonify(self._get_current_status())
        
        @self.app.route('/api/entities')
        def get_entities():
            return jsonify(self._get_entities_data())
        
        @self.app.route('/api/vulnerabilities')
        def get_vulnerabilities():
            return jsonify(self._get_vulnerabilities_data())
        
        @self.app.route('/api/attacks')
        def get_attacks():
            return jsonify(self._get_attacks_data())
        
        @self.app.route('/api/anomalies')
        def get_anomalies():
            return jsonify(self._get_anomalies_data())
        
        @self.app.route('/api/recommendations')
        def get_recommendations():
            return jsonify(self._get_recommendations_data())
        
        @self.app.route('/api/metrics')
        def get_metrics():
            return jsonify(self._get_metrics_data())
        
        @self.app.route('/api/apply_recommendation', methods=['POST'])
        def apply_recommendation():
            data = request.get_json()
            recommendation_id = data.get('recommendation_id')
            success = self._apply_recommendation(recommendation_id)
            return jsonify({'success': success})
        
        @self.app.route('/api/simulation/start', methods=['POST'])
        def start_simulation():
            if not self.simulation.running:
                self.simulation.run()
            return jsonify({'status': 'started'})
        
        @self.app.route('/api/simulation/stop', methods=['POST'])
        def stop_simulation():
            self.simulation.stop()
            return jsonify({'status': 'stopped'})
    
    def _run_dashboard(self):
        """Run the Flask dashboard"""
        host = self.config.get('dashboard.host', 'localhost')
        port = self.config.get('dashboard.port', 5000)
        debug = self.config.get('dashboard.debug', False)
        
        self.app.run(host=host, port=port, debug=debug, use_reloader=False)
    
    def _get_current_status(self) -> Dict[str, Any]:
        """Get current simulation status"""
        state = self.simulation.get_current_state()
        
        return {
            'running': state['running'],
            'current_time': state['current_time'],
            'entity_count': state['entity_count'],
            'security_score': state['metrics'].get('security_score', 0),
            'vulnerability_count': state['metrics'].get('vulnerability_count', 0),
            'attack_count': state['metrics'].get('attack_count', 0),
            'event_count': state['metrics'].get('event_count', 0)
        }
    
    def _get_entities_data(self) -> Dict[str, Any]:
        """Get entities data for visualization"""
        entities = self.simulation.entities
        
        # Group entities by type
        entity_types = {}
        for entity in entities.values():
            entity_type = entity.get('type', 'unknown')
            if entity_type not in entity_types:
                entity_types[entity_type] = []
            
            entity_types[entity_type].append({
                'id': entity['id'],
                'name': entity['name'],
                'criticality': entity.get('criticality', 'low'),
                'security_level': entity.get('security_level', 'low'),
                'network_segment': entity.get('network_segment', 'unknown'),
                'vulnerability_count': len(entity.get('vulnerabilities', [])),
                'threat_indicator_count': len(entity.get('threat_indicators', [])),
                'performance_metrics': entity.get('performance_metrics', {}),
                'security_config': entity.get('security_config', {})
            })
        
        return {
            'total_entities': len(entities),
            'entity_types': entity_types,
            'network_segments': self._get_network_segments_data(entities)
        }
    
    def _get_network_segments_data(self, entities: Dict[str, Any]) -> Dict[str, Any]:
        """Get network segments data"""
        segments = {}
        
        for entity in entities.values():
            segment = entity.get('network_segment', 'unknown')
            if segment not in segments:
                segments[segment] = {
                    'entity_count': 0,
                    'critical_entities': 0,
                    'vulnerabilities': 0
                }
            
            segments[segment]['entity_count'] += 1
            
            if entity.get('criticality') == 'high':
                segments[segment]['critical_entities'] += 1
            
            segments[segment]['vulnerabilities'] += len(entity.get('vulnerabilities', []))
        
        return segments
    
    def _get_vulnerabilities_data(self) -> Dict[str, Any]:
        """Get vulnerabilities data"""
        vulnerabilities = []
        
        for entity in self.simulation.entities.values():
            for vuln in entity.get('vulnerabilities', []):
                vulnerabilities.append({
                    'id': vuln.get('id', ''),
                    'type': vuln.get('type', 'unknown'),
                    'severity': vuln.get('severity', 'medium'),
                    'description': vuln.get('description', ''),
                    'entity_id': entity['id'],
                    'entity_name': entity['name'],
                    'entity_type': entity.get('type', 'unknown'),
                    'discovered_at': vuln.get('discovered_at', ''),
                    'status': vuln.get('status', 'open'),
                    'cvss_score': vuln.get('cvss_score', 0),
                    'exploitability': vuln.get('exploitability', 'unknown')
                })
        
        # Group by severity
        severity_groups = {}
        for vuln in vulnerabilities:
            severity = vuln['severity']
            if severity not in severity_groups:
                severity_groups[severity] = []
            severity_groups[severity].append(vuln)
        
        return {
            'total_vulnerabilities': len(vulnerabilities),
            'vulnerabilities': vulnerabilities,
            'severity_groups': severity_groups
        }
    
    def _get_attacks_data(self) -> Dict[str, Any]:
        """Get attack prediction data"""
        # Get recent security events that are attacks
        attacks = []
        
        for event in self.simulation.security_events:
            if event['type'] == 'attack':
                attacks.append({
                    'id': event['data'].get('id', ''),
                    'type': event['data'].get('type', 'unknown'),
                    'threat_actor': event['data'].get('threat_actor', 'unknown'),
                    'probability': event['data'].get('probability', 0),
                    'severity': event['data'].get('severity', 'medium'),
                    'targets': event['data'].get('targets', []),
                    'attack_path': event['data'].get('attack_path', []),
                    'impact_score': event['data'].get('impact_score', 0),
                    'detection_difficulty': event['data'].get('detection_difficulty', 'unknown'),
                    'timestamp': event['timestamp'].isoformat() if event['timestamp'] else None
                })
        
        return {
            'total_attacks': len(attacks),
            'attacks': attacks,
            'attack_types': self._group_attacks_by_type(attacks)
        }
    
    def _group_attacks_by_type(self, attacks: list) -> Dict[str, Any]:
        """Group attacks by type"""
        attack_types = {}
        
        for attack in attacks:
            attack_type = attack['type']
            if attack_type not in attack_types:
                attack_types[attack_type] = {
                    'count': 0,
                    'avg_probability': 0,
                    'avg_impact': 0,
                    'attacks': []
                }
            
            attack_types[attack_type]['count'] += 1
            attack_types[attack_type]['attacks'].append(attack)
        
        # Calculate averages
        for attack_type, data in attack_types.items():
            if data['count'] > 0:
                data['avg_probability'] = sum(a['probability'] for a in data['attacks']) / data['count']
                data['avg_impact'] = sum(a['impact_score'] for a in data['attacks']) / data['count']
        
        return attack_types
    
    def _get_anomalies_data(self) -> Dict[str, Any]:
        """Get anomaly detection data"""
        # Use the anomaly detector to get current anomalies
        anomalies = self.simulation.anomaly_detector.detect_anomalies(self.simulation.entities)
        
        return {
            'total_anomalies': len(anomalies),
            'anomalies': anomalies,
            'severity_groups': self._group_anomalies_by_severity(anomalies)
        }
    
    def _group_anomalies_by_severity(self, anomalies: list) -> Dict[str, Any]:
        """Group anomalies by severity"""
        severity_groups = {}
        
        for anomaly in anomalies:
            severity = anomaly['severity']
            if severity not in severity_groups:
                severity_groups[severity] = []
            severity_groups[severity].append(anomaly)
        
        return severity_groups
    
    def _get_recommendations_data(self) -> Dict[str, Any]:
        """Get security recommendations data"""
        # Generate recommendations using the resilience enhancer
        recommendations = self.simulation.resilience_enhancer.generate_recommendations(
            self.simulation.entities,
            self.simulation.security_events,
            self.simulation.metrics
        )
        
        return {
            'total_recommendations': len(recommendations),
            'recommendations': recommendations,
            'priority_groups': self._group_recommendations_by_priority(recommendations)
        }
    
    def _group_recommendations_by_priority(self, recommendations: list) -> Dict[str, Any]:
        """Group recommendations by priority"""
        priority_groups = {}
        
        for rec in recommendations:
            priority = rec['priority']
            if priority not in priority_groups:
                priority_groups[priority] = []
            priority_groups[priority].append(rec)
        
        return priority_groups
    
    def _get_metrics_data(self) -> Dict[str, Any]:
        """Get comprehensive metrics data"""
        metrics = self.simulation.metrics
        
        # Calculate additional metrics
        entities = self.simulation.entities
        security_events = self.simulation.security_events
        
        # Security posture metrics
        security_posture = {
            'encryption_coverage': 0,
            'authentication_coverage': 0,
            'firewall_coverage': 0,
            'patch_management_coverage': 0
        }
        
        total_entities = len(entities)
        if total_entities > 0:
            for entity in entities.values():
                security_config = entity.get('security_config', {})
                
                if security_config.get('encryption_enabled', False):
                    security_posture['encryption_coverage'] += 1
                if security_config.get('authentication_required', False):
                    security_posture['authentication_coverage'] += 1
                if security_config.get('firewall_enabled', False):
                    security_posture['firewall_coverage'] += 1
                if security_config.get('patch_management') != 'none':
                    security_posture['patch_management_coverage'] += 1
            
            # Convert to percentages
            for key in security_posture:
                security_posture[key] = (security_posture[key] / total_entities) * 100
        
        # Performance metrics
        performance_metrics = {
            'avg_cpu_usage': 0,
            'avg_memory_usage': 0,
            'avg_network_usage': 0,
            'avg_response_time': 0
        }
        
        if total_entities > 0:
            total_cpu = sum(e.get('performance_metrics', {}).get('cpu_usage', 0) for e in entities.values())
            total_memory = sum(e.get('performance_metrics', {}).get('memory_usage', 0) for e in entities.values())
            total_network = sum(e.get('performance_metrics', {}).get('network_usage', 0) for e in entities.values())
            total_response = sum(e.get('performance_metrics', {}).get('response_time', 0) for e in entities.values())
            
            performance_metrics['avg_cpu_usage'] = total_cpu / total_entities
            performance_metrics['avg_memory_usage'] = total_memory / total_entities
            performance_metrics['avg_network_usage'] = total_network / total_entities
            performance_metrics['avg_response_time'] = total_response / total_entities
        
        return {
            'current_metrics': metrics,
            'security_posture': security_posture,
            'performance_metrics': performance_metrics,
            'risk_indicators': self._calculate_risk_indicators(entities, security_events)
        }
    
    def _calculate_risk_indicators(self, entities: Dict[str, Any], security_events: list) -> Dict[str, Any]:
        """Calculate risk indicators"""
        risk_indicators = {
            'high_risk_entities': 0,
            'unencrypted_connections': 0,
            'open_vulnerabilities': 0,
            'recent_incidents': 0
        }
        
        # Count high-risk entities
        for entity in entities.values():
            if entity.get('criticality') == 'high':
                risk_indicators['high_risk_entities'] += 1
        
        # Count unencrypted connections
        for entity in entities.values():
            connectivity = entity.get('connectivity', {})
            for connection in connectivity.get('connections', []):
                if not connection.get('encrypted', False):
                    risk_indicators['unencrypted_connections'] += 1
        
        # Count open vulnerabilities
        for entity in entities.values():
            for vuln in entity.get('vulnerabilities', []):
                if vuln.get('status') == 'open':
                    risk_indicators['open_vulnerabilities'] += 1
        
        # Count recent incidents
        recent_events = [
            event for event in security_events
            if (event['timestamp'] - datetime.now()).days <= 7
        ]
        risk_indicators['recent_incidents'] = len(recent_events)
        
        return risk_indicators
    
    def _apply_recommendation(self, recommendation_id: str) -> bool:
        """Apply a security recommendation"""
        try:
            # Find the recommendation
            recommendations = self.simulation.resilience_enhancer.generate_recommendations(
                self.simulation.entities,
                self.simulation.security_events,
                self.simulation.metrics
            )
            
            for rec in recommendations:
                if rec['id'] == recommendation_id:
                    success = self.simulation.resilience_enhancer.apply_recommendation(
                        rec, self.simulation.entities
                    )
                    return success
            
            return False
        except Exception as e:
            print(f"Error applying recommendation: {e}")
            return False 