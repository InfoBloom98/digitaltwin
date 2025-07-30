"""
Resilience Enhancer for Digital Twins
"""

import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta

class ResilienceEnhancer:
    """Enhances cybersecurity resilience through recommendations and improvements"""
    
    def __init__(self, config):
        self.config = config
        self.recommendation_templates = self._initialize_recommendation_templates()
        self.improvement_strategies = self._initialize_improvement_strategies()
        
    def _initialize_recommendation_templates(self) -> Dict[str, Any]:
        """Initialize recommendation templates"""
        return {
            'encryption': {
                'title': 'Enable Encryption',
                'description': 'Enable encryption for data at rest and in transit',
                'priority': 'high',
                'effort': 'medium',
                'impact': 'high',
                'implementation': 'Configure encryption settings in security configuration'
            },
            'authentication': {
                'title': 'Implement Strong Authentication',
                'description': 'Require strong authentication for all system access',
                'priority': 'high',
                'effort': 'medium',
                'impact': 'high',
                'implementation': 'Enable authentication_required in security configuration'
            },
            'firewall': {
                'title': 'Enable Firewall Protection',
                'description': 'Enable firewall to control network traffic',
                'priority': 'medium',
                'effort': 'low',
                'impact': 'medium',
                'implementation': 'Enable firewall_enabled in security configuration'
            },
            'patch_management': {
                'title': 'Implement Automated Patch Management',
                'description': 'Set up automated patch management system',
                'priority': 'high',
                'effort': 'high',
                'impact': 'high',
                'implementation': 'Change patch_management to automatic'
            },
            'vulnerability_scanning': {
                'title': 'Enable Vulnerability Scanning',
                'description': 'Enable regular vulnerability scanning',
                'priority': 'medium',
                'effort': 'low',
                'impact': 'medium',
                'implementation': 'Enable vulnerability_scanning in security configuration'
            },
            'network_isolation': {
                'title': 'Implement Network Isolation',
                'description': 'Isolate critical systems from general network',
                'priority': 'high',
                'effort': 'high',
                'impact': 'high',
                'implementation': 'Enable network_isolation in security configuration'
            },
            'audit_logging': {
                'title': 'Enable Audit Logging',
                'description': 'Enable comprehensive audit logging',
                'priority': 'medium',
                'effort': 'low',
                'impact': 'medium',
                'implementation': 'Enable audit_logging in security configuration'
            },
            'backup_security': {
                'title': 'Secure Backup Systems',
                'description': 'Implement secure backup and recovery procedures',
                'priority': 'medium',
                'effort': 'medium',
                'impact': 'high',
                'implementation': 'Enable backup_enabled in security configuration'
            }
        }
    
    def _initialize_improvement_strategies(self) -> Dict[str, Any]:
        """Initialize improvement strategies"""
        return {
            'defense_in_depth': {
                'description': 'Implement multiple layers of security controls',
                'components': ['network_segmentation', 'access_controls', 'monitoring'],
                'priority': 'high'
            },
            'zero_trust': {
                'description': 'Implement zero trust security model',
                'components': ['identity_verification', 'least_privilege', 'continuous_monitoring'],
                'priority': 'high'
            },
            'threat_hunting': {
                'description': 'Proactively search for threats',
                'components': ['anomaly_detection', 'threat_intelligence', 'incident_response'],
                'priority': 'medium'
            },
            'security_automation': {
                'description': 'Automate security processes',
                'components': ['automated_response', 'orchestration', 'playbooks'],
                'priority': 'medium'
            }
        }
    
    def generate_recommendations(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]], 
                               metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate security recommendations based on current state"""
        recommendations = []
        
        # Analyze current security posture
        security_analysis = self._analyze_security_posture(entities, security_events, metrics)
        
        # Generate specific recommendations
        for entity_id, entity in entities.items():
            entity_recommendations = self._generate_entity_recommendations(entity, security_analysis)
            recommendations.extend(entity_recommendations)
        
        # Generate system-wide recommendations
        system_recommendations = self._generate_system_recommendations(security_analysis)
        recommendations.extend(system_recommendations)
        
        # Prioritize recommendations
        recommendations = self._prioritize_recommendations(recommendations)
        
        return recommendations
    
    def _analyze_security_posture(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]], 
                                metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze current security posture"""
        analysis = {
            'total_entities': len(entities),
            'vulnerable_entities': 0,
            'critical_vulnerabilities': 0,
            'security_gaps': [],
            'risk_factors': [],
            'compliance_issues': []
        }
        
        # Count vulnerable entities
        for entity in entities.values():
            if entity.get('vulnerabilities'):
                analysis['vulnerable_entities'] += 1
        
        # Count critical vulnerabilities
        for event in security_events:
            if (event['type'] == 'vulnerability' and 
                event['data'].get('severity') == 'critical'):
                analysis['critical_vulnerabilities'] += 1
        
        # Identify security gaps
        analysis['security_gaps'] = self._identify_security_gaps(entities)
        
        # Identify risk factors
        analysis['risk_factors'] = self._identify_risk_factors(entities, security_events)
        
        # Identify compliance issues
        analysis['compliance_issues'] = self._identify_compliance_issues(entities)
        
        return analysis
    
    def _identify_security_gaps(self, entities: Dict[str, Any]) -> List[str]:
        """Identify security gaps across entities"""
        gaps = []
        
        # Check for common security gaps
        encryption_disabled = 0
        auth_disabled = 0
        firewall_disabled = 0
        patch_disabled = 0
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            
            if not security_config.get('encryption_enabled', False):
                encryption_disabled += 1
            if not security_config.get('authentication_required', False):
                auth_disabled += 1
            if not security_config.get('firewall_enabled', False):
                firewall_disabled += 1
            if security_config.get('patch_management') == 'none':
                patch_disabled += 1
        
        total_entities = len(entities)
        if total_entities > 0:
            if encryption_disabled / total_entities > 0.5:
                gaps.append('encryption_coverage')
            if auth_disabled / total_entities > 0.5:
                gaps.append('authentication_coverage')
            if firewall_disabled / total_entities > 0.5:
                gaps.append('firewall_coverage')
            if patch_disabled / total_entities > 0.5:
                gaps.append('patch_management')
        
        return gaps
    
    def _identify_risk_factors(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> List[str]:
        """Identify risk factors"""
        risk_factors = []
        
        # Check for high-risk entities
        critical_entities = 0
        for entity in entities.values():
            if entity.get('criticality') == 'high':
                critical_entities += 1
        
        if critical_entities > 0:
            risk_factors.append('critical_systems_exposed')
        
        # Check for recent security events
        recent_events = [
            event for event in security_events
            if (datetime.now() - event['timestamp']).days <= 7
        ]
        
        if len(recent_events) > 5:
            risk_factors.append('high_security_incidents')
        
        # Check for unencrypted connections
        unencrypted_connections = 0
        for entity in entities.values():
            connectivity = entity.get('connectivity', {})
            for connection in connectivity.get('connections', []):
                if not connection.get('encrypted', False):
                    unencrypted_connections += 1
        
        if unencrypted_connections > 0:
            risk_factors.append('unencrypted_communications')
        
        return risk_factors
    
    def _identify_compliance_issues(self, entities: Dict[str, Any]) -> List[str]:
        """Identify compliance issues"""
        compliance_issues = []
        
        # Check HIPAA compliance
        hipaa_compliant = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if (security_config.get('encryption_enabled', False) and 
                security_config.get('authentication_required', False) and
                security_config.get('audit_logging', False)):
                hipaa_compliant += 1
        
        if total_entities > 0 and hipaa_compliant / total_entities < 0.8:
            compliance_issues.append('hipaa_compliance')
        
        return compliance_issues
    
    def _generate_entity_recommendations(self, entity: Dict[str, Any], security_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate recommendations for a specific entity"""
        recommendations = []
        security_config = entity.get('security_config', {})
        
        # Check encryption
        if not security_config.get('encryption_enabled', False):
            recommendations.append(self._create_recommendation('encryption', entity))
        
        # Check authentication
        if not security_config.get('authentication_required', False):
            recommendations.append(self._create_recommendation('authentication', entity))
        
        # Check firewall
        if not security_config.get('firewall_enabled', False):
            recommendations.append(self._create_recommendation('firewall', entity))
        
        # Check patch management
        if security_config.get('patch_management') == 'none':
            recommendations.append(self._create_recommendation('patch_management', entity))
        
        # Check vulnerability scanning
        if not security_config.get('vulnerability_scanning', False):
            recommendations.append(self._create_recommendation('vulnerability_scanning', entity))
        
        # Check network isolation for critical systems
        if (entity.get('criticality') == 'high' and 
            not security_config.get('network_isolation', False)):
            recommendations.append(self._create_recommendation('network_isolation', entity))
        
        # Check audit logging
        if not security_config.get('audit_logging', False):
            recommendations.append(self._create_recommendation('audit_logging', entity))
        
        # Check backup
        if not security_config.get('backup_enabled', False):
            recommendations.append(self._create_recommendation('backup_security', entity))
        
        return recommendations
    
    def _generate_system_recommendations(self, security_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate system-wide recommendations"""
        recommendations = []
        
        # Recommend based on security gaps
        for gap in security_analysis['security_gaps']:
            if gap == 'encryption_coverage':
                recommendations.append(self._create_system_recommendation('encryption'))
            elif gap == 'authentication_coverage':
                recommendations.append(self._create_system_recommendation('authentication'))
            elif gap == 'firewall_coverage':
                recommendations.append(self._create_system_recommendation('firewall'))
            elif gap == 'patch_management':
                recommendations.append(self._create_system_recommendation('patch_management'))
        
        # Recommend based on risk factors
        for risk_factor in security_analysis['risk_factors']:
            if risk_factor == 'critical_systems_exposed':
                recommendations.append(self._create_system_recommendation('network_isolation'))
            elif risk_factor == 'unencrypted_communications':
                recommendations.append(self._create_system_recommendation('encryption'))
        
        # Recommend based on compliance issues
        for compliance_issue in security_analysis['compliance_issues']:
            if compliance_issue == 'hipaa_compliance':
                recommendations.extend([
                    self._create_system_recommendation('encryption'),
                    self._create_system_recommendation('authentication'),
                    self._create_system_recommendation('audit_logging')
                ])
        
        return recommendations
    
    def _create_recommendation(self, rec_type: str, entity: Dict[str, Any]) -> Dict[str, Any]:
        """Create a recommendation for a specific entity"""
        template = self.recommendation_templates[rec_type]
        
        return {
            'id': f"{rec_type}_{entity['id']}",
            'type': rec_type,
            'title': template['title'],
            'description': template['description'],
            'priority': template['priority'],
            'effort': template['effort'],
            'impact': template['impact'],
            'implementation': template['implementation'],
            'target_entity': entity['id'],
            'target_system': entity['name'],
            'status': 'pending',
            'created_at': datetime.now(),
            'estimated_completion': None
        }
    
    def _create_system_recommendation(self, rec_type: str) -> Dict[str, Any]:
        """Create a system-wide recommendation"""
        template = self.recommendation_templates[rec_type]
        
        return {
            'id': f"{rec_type}_system_wide",
            'type': rec_type,
            'title': f"System-wide {template['title']}",
            'description': f"Apply {template['description']} across all systems",
            'priority': template['priority'],
            'effort': 'high' if template['effort'] == 'high' else 'medium',
            'impact': template['impact'],
            'implementation': f"Apply {template['implementation']} to all entities",
            'target_entity': 'system_wide',
            'target_system': 'all_systems',
            'status': 'pending',
            'created_at': datetime.now(),
            'estimated_completion': None
        }
    
    def _prioritize_recommendations(self, recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Prioritize recommendations based on priority, effort, and impact"""
        for rec in recommendations:
            # Calculate priority score
            priority_scores = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
            effort_scores = {'low': 3, 'medium': 2, 'high': 1}
            impact_scores = {'low': 1, 'medium': 2, 'high': 3}
            
            priority_score = priority_scores.get(rec['priority'], 1)
            effort_score = effort_scores.get(rec['effort'], 2)
            impact_score = impact_scores.get(rec['impact'], 2)
            
            # Calculate overall score (higher is better)
            rec['priority_score'] = priority_score * impact_score * effort_score
        
        # Sort by priority score (descending)
        recommendations.sort(key=lambda x: x['priority_score'], reverse=True)
        
        return recommendations
    
    def apply_recommendation(self, recommendation: Dict[str, Any], entities: Dict[str, Any]) -> bool:
        """Apply a security recommendation"""
        try:
            if recommendation['target_entity'] == 'system_wide':
                # Apply to all entities
                for entity in entities.values():
                    self._apply_to_entity(recommendation, entity)
            else:
                # Apply to specific entity
                entity = entities.get(recommendation['target_entity'])
                if entity:
                    self._apply_to_entity(recommendation, entity)
            
            # Update recommendation status
            recommendation['status'] = 'applied'
            recommendation['applied_at'] = datetime.now()
            
            return True
            
        except Exception as e:
            recommendation['status'] = 'failed'
            recommendation['error'] = str(e)
            return False
    
    def _apply_to_entity(self, recommendation: Dict[str, Any], entity: Dict[str, Any]):
        """Apply recommendation to a specific entity"""
        rec_type = recommendation['type']
        security_config = entity.get('security_config', {})
        
        if rec_type == 'encryption':
            security_config['encryption_enabled'] = True
        elif rec_type == 'authentication':
            security_config['authentication_required'] = True
        elif rec_type == 'firewall':
            security_config['firewall_enabled'] = True
        elif rec_type == 'patch_management':
            security_config['patch_management'] = 'automatic'
        elif rec_type == 'vulnerability_scanning':
            security_config['vulnerability_scanning'] = True
        elif rec_type == 'network_isolation':
            security_config['network_isolation'] = True
        elif rec_type == 'audit_logging':
            security_config['audit_logging'] = True
        elif rec_type == 'backup_security':
            security_config['backup_enabled'] = True
        
        entity['security_config'] = security_config
        entity['last_updated'] = datetime.now()
    
    def generate_improvement_plan(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]], 
                                metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive improvement plan"""
        recommendations = self.generate_recommendations(entities, security_events, metrics)
        
        improvement_plan = {
            'current_state': {
                'security_score': metrics.get('security_score', 0),
                'vulnerability_count': len([e for e in security_events if e['type'] == 'vulnerability']),
                'entity_count': len(entities)
            },
            'recommendations': recommendations,
            'strategies': self._select_improvement_strategies(recommendations),
            'timeline': self._generate_timeline(recommendations),
            'expected_improvements': self._calculate_expected_improvements(recommendations),
            'created_at': datetime.now()
        }
        
        return improvement_plan
    
    def _select_improvement_strategies(self, recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Select appropriate improvement strategies"""
        strategies = []
        
        # Select strategies based on recommendation types
        rec_types = [rec['type'] for rec in recommendations]
        
        if 'encryption' in rec_types and 'authentication' in rec_types:
            strategies.append(self.improvement_strategies['zero_trust'])
        
        if 'network_isolation' in rec_types:
            strategies.append(self.improvement_strategies['defense_in_depth'])
        
        if 'vulnerability_scanning' in rec_types:
            strategies.append(self.improvement_strategies['threat_hunting'])
        
        return strategies
    
    def _generate_timeline(self, recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate implementation timeline"""
        timeline = []
        
        # Group recommendations by priority
        high_priority = [rec for rec in recommendations if rec['priority'] == 'high']
        medium_priority = [rec for rec in recommendations if rec['priority'] == 'medium']
        low_priority = [rec for rec in recommendations if rec['priority'] == 'low']
        
        # Schedule high priority for immediate implementation
        for rec in high_priority:
            timeline.append({
                'recommendation_id': rec['id'],
                'phase': 'immediate',
                'estimated_duration': '1-2 weeks',
                'dependencies': []
            })
        
        # Schedule medium priority for short term
        for rec in medium_priority:
            timeline.append({
                'recommendation_id': rec['id'],
                'phase': 'short_term',
                'estimated_duration': '2-4 weeks',
                'dependencies': []
            })
        
        # Schedule low priority for long term
        for rec in low_priority:
            timeline.append({
                'recommendation_id': rec['id'],
                'phase': 'long_term',
                'estimated_duration': '1-3 months',
                'dependencies': []
            })
        
        return timeline
    
    def _calculate_expected_improvements(self, recommendations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate expected improvements from recommendations"""
        improvements = {
            'security_score_increase': 0,
            'vulnerability_reduction': 0,
            'compliance_improvement': 0,
            'risk_reduction': 0
        }
        
        for rec in recommendations:
            if rec['impact'] == 'high':
                improvements['security_score_increase'] += 10
                improvements['vulnerability_reduction'] += 2
            elif rec['impact'] == 'medium':
                improvements['security_score_increase'] += 5
                improvements['vulnerability_reduction'] += 1
        
        # Cap improvements
        improvements['security_score_increase'] = min(improvements['security_score_increase'], 50)
        improvements['vulnerability_reduction'] = min(improvements['vulnerability_reduction'], 20)
        
        return improvements 