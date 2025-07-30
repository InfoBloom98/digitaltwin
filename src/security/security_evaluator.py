"""
Security Evaluator for Digital Twins
"""

import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta

class SecurityEvaluator:
    """Evaluates security posture and effectiveness of security measures"""
    
    def __init__(self, config):
        self.config = config
        self.evaluation_criteria = self._initialize_evaluation_criteria()
        self.security_frameworks = self._initialize_security_frameworks()
        
    def _initialize_evaluation_criteria(self) -> Dict[str, Any]:
        """Initialize security evaluation criteria"""
        return {
            'access_control': {
                'weight': 0.25,
                'metrics': ['authentication_strength', 'authorization_coverage', 'privilege_management'],
                'max_score': 100
            },
            'data_protection': {
                'weight': 0.20,
                'metrics': ['encryption_coverage', 'data_classification', 'backup_security'],
                'max_score': 100
            },
            'network_security': {
                'weight': 0.20,
                'metrics': ['firewall_coverage', 'network_segmentation', 'intrusion_detection'],
                'max_score': 100
            },
            'vulnerability_management': {
                'weight': 0.15,
                'metrics': ['patch_management', 'vulnerability_scanning', 'penetration_testing'],
                'max_score': 100
            },
            'incident_response': {
                'weight': 0.10,
                'metrics': ['detection_capability', 'response_time', 'recovery_procedures'],
                'max_score': 100
            },
            'compliance': {
                'weight': 0.10,
                'metrics': ['regulatory_compliance', 'audit_trail', 'documentation'],
                'max_score': 100
            }
        }
    
    def _initialize_security_frameworks(self) -> Dict[str, Any]:
        """Initialize security frameworks for evaluation"""
        return {
            'nist_cybersecurity': {
                'identify': ['asset_management', 'business_environment', 'governance'],
                'protect': ['access_control', 'awareness_training', 'data_security'],
                'detect': ['anomalies_events', 'security_monitoring', 'detection_processes'],
                'respond': ['response_planning', 'communications', 'analysis'],
                'recover': ['recovery_planning', 'improvements', 'communications']
            },
            'iso_27001': {
                'information_security_policies': ['policy_framework', 'policy_review'],
                'organization_of_information_security': ['roles_responsibilities', 'authorization'],
                'human_resource_security': ['screening', 'terms_conditions', 'training'],
                'asset_management': ['inventory', 'ownership', 'acceptable_use'],
                'access_control': ['access_policy', 'user_access_management', 'system_access']
            },
            'hipaa': {
                'administrative_safeguards': ['security_officer', 'workforce_security', 'training'],
                'physical_safeguards': ['facility_access', 'workstation_security', 'device_control'],
                'technical_safeguards': ['access_control', 'audit_controls', 'integrity']
            }
        }
    
    def evaluate_security(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> float:
        """Evaluate overall security posture"""
        evaluation_results = {}
        
        # Evaluate each security domain
        for domain, criteria in self.evaluation_criteria.items():
            domain_score = self._evaluate_domain(domain, criteria, entities, security_events)
            evaluation_results[domain] = domain_score
        
        # Calculate weighted overall score
        overall_score = self._calculate_weighted_score(evaluation_results)
        
        # Apply risk adjustments
        risk_adjusted_score = self._apply_risk_adjustments(overall_score, security_events)
        
        return risk_adjusted_score
    
    def _evaluate_domain(self, domain: str, criteria: Dict[str, Any], 
                        entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> float:
        """Evaluate a specific security domain"""
        metrics = criteria['metrics']
        max_score = criteria['max_score']
        
        domain_scores = []
        
        for metric in metrics:
            metric_score = self._evaluate_metric(domain, metric, entities, security_events)
            domain_scores.append(metric_score)
        
        # Calculate average score for the domain
        domain_score = np.mean(domain_scores) if domain_scores else 0
        
        return min(domain_score, max_score)
    
    def _evaluate_metric(self, domain: str, metric: str, entities: Dict[str, Any], 
                        security_events: List[Dict[str, Any]]) -> float:
        """Evaluate a specific security metric"""
        
        if domain == 'access_control':
            return self._evaluate_access_control_metric(metric, entities)
        elif domain == 'data_protection':
            return self._evaluate_data_protection_metric(metric, entities)
        elif domain == 'network_security':
            return self._evaluate_network_security_metric(metric, entities)
        elif domain == 'vulnerability_management':
            return self._evaluate_vulnerability_management_metric(metric, entities, security_events)
        elif domain == 'incident_response':
            return self._evaluate_incident_response_metric(metric, entities, security_events)
        elif domain == 'compliance':
            return self._evaluate_compliance_metric(metric, entities)
        
        return 0.0
    
    def _evaluate_access_control_metric(self, metric: str, entities: Dict[str, Any]) -> float:
        """Evaluate access control metrics"""
        if metric == 'authentication_strength':
            return self._assess_authentication_strength(entities)
        elif metric == 'authorization_coverage':
            return self._assess_authorization_coverage(entities)
        elif metric == 'privilege_management':
            return self._assess_privilege_management(entities)
        
        return 0.0
    
    def _evaluate_data_protection_metric(self, metric: str, entities: Dict[str, Any]) -> float:
        """Evaluate data protection metrics"""
        if metric == 'encryption_coverage':
            return self._assess_encryption_coverage(entities)
        elif metric == 'data_classification':
            return self._assess_data_classification(entities)
        elif metric == 'backup_security':
            return self._assess_backup_security(entities)
        
        return 0.0
    
    def _evaluate_network_security_metric(self, metric: str, entities: Dict[str, Any]) -> float:
        """Evaluate network security metrics"""
        if metric == 'firewall_coverage':
            return self._assess_firewall_coverage(entities)
        elif metric == 'network_segmentation':
            return self._assess_network_segmentation(entities)
        elif metric == 'intrusion_detection':
            return self._assess_intrusion_detection(entities)
        
        return 0.0
    
    def _evaluate_vulnerability_management_metric(self, metric: str, entities: Dict[str, Any], 
                                                security_events: List[Dict[str, Any]]) -> float:
        """Evaluate vulnerability management metrics"""
        if metric == 'patch_management':
            return self._assess_patch_management(entities)
        elif metric == 'vulnerability_scanning':
            return self._assess_vulnerability_scanning(entities)
        elif metric == 'penetration_testing':
            return self._assess_penetration_testing(entities, security_events)
        
        return 0.0
    
    def _evaluate_incident_response_metric(self, metric: str, entities: Dict[str, Any], 
                                         security_events: List[Dict[str, Any]]) -> float:
        """Evaluate incident response metrics"""
        if metric == 'detection_capability':
            return self._assess_detection_capability(entities, security_events)
        elif metric == 'response_time':
            return self._assess_response_time(security_events)
        elif metric == 'recovery_procedures':
            return self._assess_recovery_procedures(entities)
        
        return 0.0
    
    def _evaluate_compliance_metric(self, metric: str, entities: Dict[str, Any]) -> float:
        """Evaluate compliance metrics"""
        if metric == 'regulatory_compliance':
            return self._assess_regulatory_compliance(entities)
        elif metric == 'audit_trail':
            return self._assess_audit_trail(entities)
        elif metric == 'documentation':
            return self._assess_documentation(entities)
        
        return 0.0
    
    # Access Control Assessments
    def _assess_authentication_strength(self, entities: Dict[str, Any]) -> float:
        """Assess authentication strength across entities"""
        auth_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('authentication_required', False):
                auth_enabled += 1
        
        return (auth_enabled / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_authorization_coverage(self, entities: Dict[str, Any]) -> float:
        """Assess authorization coverage"""
        role_based_auth = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('access_control') == 'role_based':
                role_based_auth += 1
        
        return (role_based_auth / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_privilege_management(self, entities: Dict[str, Any]) -> float:
        """Assess privilege management"""
        # Simplified assessment based on security configurations
        privileged_entities = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            if entity.get('criticality') == 'high':
                security_config = entity.get('security_config', {})
                if (security_config.get('authentication_required', False) and 
                    security_config.get('access_control') != 'none'):
                    privileged_entities += 1
        
        return (privileged_entities / total_entities) * 100 if total_entities > 0 else 0
    
    # Data Protection Assessments
    def _assess_encryption_coverage(self, entities: Dict[str, Any]) -> float:
        """Assess encryption coverage"""
        encrypted_entities = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('encryption_enabled', False):
                encrypted_entities += 1
        
        return (encrypted_entities / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_data_classification(self, entities: Dict[str, Any]) -> float:
        """Assess data classification implementation"""
        classified_entities = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            if entity.get('security_level') in ['high', 'critical']:
                classified_entities += 1
        
        return (classified_entities / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_backup_security(self, entities: Dict[str, Any]) -> float:
        """Assess backup security"""
        backup_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('backup_enabled', False):
                backup_enabled += 1
        
        return (backup_enabled / total_entities) * 100 if total_entities > 0 else 0
    
    # Network Security Assessments
    def _assess_firewall_coverage(self, entities: Dict[str, Any]) -> float:
        """Assess firewall coverage"""
        firewall_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('firewall_enabled', False):
                firewall_enabled += 1
        
        return (firewall_enabled / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_network_segmentation(self, entities: Dict[str, Any]) -> float:
        """Assess network segmentation"""
        segmented_entities = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            if entity.get('network_segment') != 'default':
                segmented_entities += 1
        
        return (segmented_entities / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_intrusion_detection(self, entities: Dict[str, Any]) -> float:
        """Assess intrusion detection coverage"""
        ids_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('intrusion_detection', False):
                ids_enabled += 1
        
        return (ids_enabled / total_entities) * 100 if total_entities > 0 else 0
    
    # Vulnerability Management Assessments
    def _assess_patch_management(self, entities: Dict[str, Any]) -> float:
        """Assess patch management"""
        patch_managed = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('patch_management') == 'automatic':
                patch_managed += 1
        
        return (patch_managed / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_vulnerability_scanning(self, entities: Dict[str, Any]) -> float:
        """Assess vulnerability scanning coverage"""
        scanning_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('vulnerability_scanning', False):
                scanning_enabled += 1
        
        return (scanning_enabled / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_penetration_testing(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> float:
        """Assess penetration testing effectiveness"""
        # Simplified assessment based on security events
        recent_events = [
            event for event in security_events
            if (datetime.now() - event['timestamp']).days <= 30
        ]
        
        if len(recent_events) > 0:
            # Higher score if vulnerabilities are being detected and addressed
            return min(len(recent_events) * 10, 100)
        
        return 50  # Baseline score
    
    # Incident Response Assessments
    def _assess_detection_capability(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> float:
        """Assess detection capability"""
        detection_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('intrusion_detection', False):
                detection_enabled += 1
        
        base_score = (detection_enabled / total_entities) * 100 if total_entities > 0 else 0
        
        # Bonus for recent detections
        recent_detections = len([e for e in security_events if e['type'] == 'vulnerability'])
        bonus = min(recent_detections * 5, 20)
        
        return min(base_score + bonus, 100)
    
    def _assess_response_time(self, security_events: List[Dict[str, Any]]) -> float:
        """Assess incident response time"""
        # Simplified assessment - in real implementation, would track actual response times
        if len(security_events) > 0:
            return 75  # Assume reasonable response time
        return 50  # Baseline score
    
    def _assess_recovery_procedures(self, entities: Dict[str, Any]) -> float:
        """Assess recovery procedures"""
        recovery_ready = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if (security_config.get('backup_enabled', False) and 
                security_config.get('audit_logging', False)):
                recovery_ready += 1
        
        return (recovery_ready / total_entities) * 100 if total_entities > 0 else 0
    
    # Compliance Assessments
    def _assess_regulatory_compliance(self, entities: Dict[str, Any]) -> float:
        """Assess regulatory compliance"""
        # Simplified HIPAA compliance assessment
        hipaa_compliant = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if (security_config.get('encryption_enabled', False) and 
                security_config.get('authentication_required', False) and
                security_config.get('audit_logging', False)):
                hipaa_compliant += 1
        
        return (hipaa_compliant / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_audit_trail(self, entities: Dict[str, Any]) -> float:
        """Assess audit trail implementation"""
        audit_enabled = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if security_config.get('audit_logging', False):
                audit_enabled += 1
        
        return (audit_enabled / total_entities) * 100 if total_entities > 0 else 0
    
    def _assess_documentation(self, entities: Dict[str, Any]) -> float:
        """Assess security documentation"""
        # Simplified assessment - assume good documentation if security configs are comprehensive
        documented_entities = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            if len(security_config) >= 8:  # Assume comprehensive config indicates good documentation
                documented_entities += 1
        
        return (documented_entities / total_entities) * 100 if total_entities > 0 else 0
    
    def _calculate_weighted_score(self, evaluation_results: Dict[str, float]) -> float:
        """Calculate weighted overall security score"""
        weighted_sum = 0
        total_weight = 0
        
        for domain, score in evaluation_results.items():
            weight = self.evaluation_criteria[domain]['weight']
            weighted_sum += score * weight
            total_weight += weight
        
        return weighted_sum / total_weight if total_weight > 0 else 0
    
    def _apply_risk_adjustments(self, base_score: float, security_events: List[Dict[str, Any]]) -> float:
        """Apply risk-based adjustments to the security score"""
        adjusted_score = base_score
        
        # Reduce score for recent critical vulnerabilities
        critical_vulns = [
            event for event in security_events
            if (event['type'] == 'vulnerability' and 
                event['data'].get('severity') == 'critical' and
                (datetime.now() - event['timestamp']).days <= 7)
        ]
        
        adjusted_score -= len(critical_vulns) * 5
        
        # Reduce score for high-severity vulnerabilities
        high_vulns = [
            event for event in security_events
            if (event['type'] == 'vulnerability' and 
                event['data'].get('severity') == 'high' and
                (datetime.now() - event['timestamp']).days <= 30)
        ]
        
        adjusted_score -= len(high_vulns) * 2
        
        return max(adjusted_score, 0)  # Ensure score doesn't go below 0 