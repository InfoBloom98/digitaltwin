"""
Core simulation engine for cybersecurity evaluation
"""

import time
import threading
from typing import Dict, List, Any
from datetime import datetime, timedelta
import numpy as np

from utils.logger import SecurityLogger, PerformanceLogger
from data.digital_twin_generator import DigitalTwinGenerator
from security.vulnerability_detector import VulnerabilityDetector
from security.attack_predictor import AttackPredictor
from security.security_evaluator import SecurityEvaluator
from security.resilience_enhancer import ResilienceEnhancer
from models.anomaly_detector import AnomalyDetector

class SimulationEngine:
    """Main simulation engine for cybersecurity evaluation"""
    
    def __init__(self, config):
        self.config = config
        self.logger = SecurityLogger()
        self.performance_logger = PerformanceLogger()
        
        # Simulation state
        self.running = False
        self.start_time = None
        self.current_time = 0
        self.entities = {}
        self.security_events = []
        self.metrics = {}
        
        # Initialize components
        self._initialize_components()
        
        # Threading
        self.simulation_thread = None
        self.monitoring_thread = None
        
    def _initialize_components(self):
        """Initialize all simulation components"""
        try:
            # Data generation
            self.digital_twin_generator = DigitalTwinGenerator(self.config)
            
            # Security components
            self.vulnerability_detector = VulnerabilityDetector(self.config)
            self.attack_predictor = AttackPredictor(self.config)
            self.security_evaluator = SecurityEvaluator(self.config)
            self.resilience_enhancer = ResilienceEnhancer(self.config)
            
            # ML models
            self.anomaly_detector = AnomalyDetector(self.config)
            
            self.logger.logger.info("All simulation components initialized successfully")
            
        except Exception as e:
            self.logger.logger.error(f"Error initializing components: {e}")
            raise
    
    def run(self):
        """Start the simulation"""
        self.running = True
        self.start_time = datetime.now()
        self.current_time = 0
        
        self.logger.logger.info("Starting cybersecurity simulation")
        
        # Start monitoring thread
        self.monitoring_thread = threading.Thread(target=self._monitor_system)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
        
        # Main simulation loop
        try:
            while self.running and self.current_time < self.config.get('simulation.duration', 3600):
                self._simulation_step()
                time.sleep(self.config.get('simulation.update_interval', 1))
                self.current_time += self.config.get('simulation.update_interval', 1)
                
        except KeyboardInterrupt:
            self.logger.logger.info("Simulation interrupted by user")
        finally:
            self.stop()
    
    def _simulation_step(self):
        """Execute one simulation step"""
        try:
            # Generate/update digital twins
            self._update_digital_twins()
            
            # Detect vulnerabilities
            self._detect_vulnerabilities()
            
            # Predict attacks
            self._predict_attacks()
            
            # Evaluate security
            self._evaluate_security()
            
            # Enhance resilience
            self._enhance_resilience()
            
            # Update metrics
            self._update_metrics()
            
        except Exception as e:
            self.logger.logger.error(f"Error in simulation step: {e}")
    
    def _update_digital_twins(self):
        """Update digital twin entities"""
        # Generate new entities if needed
        if len(self.entities) < self.config.get('simulation.max_entities', 1000):
            new_entities = self.digital_twin_generator.generate_entities(10)
            for entity in new_entities:
                self.entities[entity['id']] = entity
        
        # Update existing entities
        for entity_id, entity in self.entities.items():
            updated_entity = self.digital_twin_generator.update_entity(entity)
            self.entities[entity_id] = updated_entity
    
    def _detect_vulnerabilities(self):
        """Detect vulnerabilities in digital twins"""
        vulnerabilities = self.vulnerability_detector.detect_vulnerabilities(self.entities)
        
        for vuln in vulnerabilities:
            self.logger.log_vulnerability(
                vuln['type'],
                vuln['severity'],
                vuln['description'],
                vuln['affected_system']
            )
            self.security_events.append({
                'timestamp': datetime.now(),
                'type': 'vulnerability',
                'data': vuln
            })
    
    def _predict_attacks(self):
        """Predict potential attack scenarios"""
        attack_scenarios = self.attack_predictor.predict_attacks(self.entities, self.security_events)
        
        for scenario in attack_scenarios:
            if scenario['probability'] > 0.7:  # High probability attacks
                self.logger.log_threat_intelligence(
                    scenario['type'],
                    scenario['probability'],
                    scenario['source'],
                    scenario['indicators']
                )
    
    def _evaluate_security(self):
        """Evaluate current security posture"""
        security_score = self.security_evaluator.evaluate_security(
            self.entities, 
            self.security_events
        )
        
        self.metrics['security_score'] = security_score
        
        # Log significant changes
        if 'previous_security_score' in self.metrics:
            change = security_score - self.metrics['previous_security_score']
            if abs(change) > 0.1:
                self.logger.logger.info(f"Security score changed by {change:.3f}")
        
        self.metrics['previous_security_score'] = security_score
    
    def _enhance_resilience(self):
        """Enhance cybersecurity resilience"""
        recommendations = self.resilience_enhancer.generate_recommendations(
            self.entities,
            self.security_events,
            self.metrics
        )
        
        # Apply high-priority recommendations
        for rec in recommendations:
            if rec['priority'] == 'high':
                self.resilience_enhancer.apply_recommendation(rec, self.entities)
                self.logger.logger.info(f"Applied high-priority recommendation: {rec['title']}")
    
    def _update_metrics(self):
        """Update simulation metrics"""
        self.metrics.update({
            'current_time': self.current_time,
            'entity_count': len(self.entities),
            'event_count': len(self.security_events),
            'vulnerability_count': len([e for e in self.security_events if e['type'] == 'vulnerability']),
            'attack_count': len([e for e in self.security_events if e['type'] == 'attack'])
        })
    
    def _monitor_system(self):
        """Monitor system performance and health"""
        while self.running:
            try:
                # Monitor resource usage
                cpu_usage = self._get_cpu_usage()
                memory_usage = self._get_memory_usage()
                network_usage = self._get_network_usage()
                
                self.performance_logger.log_resource_usage(
                    cpu_usage, memory_usage, network_usage
                )
                
                # Check for system health issues
                if cpu_usage > 90 or memory_usage > 90:
                    self.logger.log_incident(
                        'system_overload',
                        'high',
                        f'High resource usage: CPU {cpu_usage}%, Memory {memory_usage}%',
                        0
                    )
                
                time.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                self.logger.logger.error(f"Error in system monitoring: {e}")
    
    def _get_cpu_usage(self) -> float:
        """Get current CPU usage percentage"""
        try:
            import psutil
            return psutil.cpu_percent()
        except ImportError:
            return np.random.uniform(20, 60)  # Simulated value
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage percentage"""
        try:
            import psutil
            return psutil.virtual_memory().percent
        except ImportError:
            return np.random.uniform(30, 70)  # Simulated value
    
    def _get_network_usage(self) -> float:
        """Get current network usage percentage"""
        try:
            import psutil
            net_io = psutil.net_io_counters()
            return (net_io.bytes_sent + net_io.bytes_recv) / (1024 * 1024)  # MB
        except ImportError:
            return np.random.uniform(1, 10)  # Simulated value
    
    def stop(self):
        """Stop the simulation"""
        self.running = False
        self.logger.logger.info("Simulation stopped")
        
        # Generate final report
        self._generate_final_report()
    
    def _generate_final_report(self):
        """Generate final simulation report"""
        report = {
            'simulation_duration': self.current_time,
            'total_entities': len(self.entities),
            'total_events': len(self.security_events),
            'final_security_score': self.metrics.get('security_score', 0),
            'vulnerabilities_detected': len([e for e in self.security_events if e['type'] == 'vulnerability']),
            'attacks_predicted': len([e for e in self.security_events if e['type'] == 'attack']),
            'recommendations_applied': len([e for e in self.security_events if e['type'] == 'recommendation'])
        }
        
        self.logger.logger.info(f"Final simulation report: {report}")
        return report
    
    def get_current_state(self) -> Dict[str, Any]:
        """Get current simulation state for dashboard"""
        return {
            'running': self.running,
            'current_time': self.current_time,
            'entity_count': len(self.entities),
            'metrics': self.metrics,
            'recent_events': self.security_events[-10:] if self.security_events else []
        } 