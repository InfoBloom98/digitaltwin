"""
Attack Prediction System for Digital Twins
"""

import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta
import random

class AttackPredictor:
    """Predicts potential cyberattack scenarios"""
    
    def __init__(self, config):
        self.config = config
        self.attack_types = self._initialize_attack_types()
        self.threat_actors = self._initialize_threat_actors()
        self.attack_patterns = self._initialize_attack_patterns()
        
    def _initialize_attack_types(self) -> Dict[str, Any]:
        """Initialize different types of cyberattacks"""
        return {
            'ransomware': {
                'probability_base': 0.15,
                'severity': 'critical',
                'indicators': ['file_encryption', 'ransom_note', 'network_spread'],
                'targets': ['patient_data', 'medical_devices', 'hospital_systems'],
                'impact': 'data_loss, operational_disruption'
            },
            'data_breach': {
                'probability_base': 0.25,
                'severity': 'high',
                'indicators': ['unauthorized_access', 'data_exfiltration', 'suspicious_activity'],
                'targets': ['patient_records', 'financial_data', 'research_data'],
                'impact': 'privacy_violation, regulatory_penalties'
            },
            'denial_of_service': {
                'probability_base': 0.20,
                'severity': 'medium',
                'indicators': ['high_traffic', 'service_unavailability', 'resource_exhaustion'],
                'targets': ['web_services', 'network_infrastructure', 'medical_devices'],
                'impact': 'service_disruption, operational_impact'
            },
            'insider_threat': {
                'probability_base': 0.10,
                'severity': 'high',
                'indicators': ['privilege_abuse', 'data_access_patterns', 'behavioral_changes'],
                'targets': ['sensitive_data', 'system_access', 'financial_systems'],
                'impact': 'data_theft, system_compromise'
            },
            'advanced_persistent_threat': {
                'probability_base': 0.05,
                'severity': 'critical',
                'indicators': ['stealth_activity', 'long_term_presence', 'sophisticated_tools'],
                'targets': ['intellectual_property', 'research_data', 'critical_infrastructure'],
                'impact': 'long_term_compromise, data_theft'
            },
            'medical_device_hijacking': {
                'probability_base': 0.12,
                'severity': 'critical',
                'indicators': ['device_malfunction', 'unauthorized_control', 'data_manipulation'],
                'targets': ['patient_monitors', 'life_support_systems', 'diagnostic_equipment'],
                'impact': 'patient_safety, medical_errors'
            }
        }
    
    def _initialize_threat_actors(self) -> Dict[str, Any]:
        """Initialize threat actor profiles"""
        return {
            'cybercriminals': {
                'motivation': 'financial_gain',
                'capability': 'medium',
                'persistence': 'low',
                'target_preference': ['financial_data', 'patient_records']
            },
            'nation_state': {
                'motivation': 'espionage',
                'capability': 'high',
                'persistence': 'high',
                'target_preference': ['research_data', 'intellectual_property', 'critical_infrastructure']
            },
            'hacktivists': {
                'motivation': 'ideological',
                'capability': 'medium',
                'persistence': 'medium',
                'target_preference': ['public_systems', 'administrative_data']
            },
            'insiders': {
                'motivation': 'personal_gain',
                'capability': 'high',
                'persistence': 'medium',
                'target_preference': ['sensitive_data', 'financial_systems']
            },
            'medical_device_hackers': {
                'motivation': 'research_curiosity',
                'capability': 'high',
                'persistence': 'low',
                'target_preference': ['medical_devices', 'patient_monitors']
            }
        }
    
    def _initialize_attack_patterns(self) -> Dict[str, Any]:
        """Initialize attack patterns and indicators"""
        return {
            'reconnaissance': {
                'indicators': ['port_scanning', 'network_mapping', 'vulnerability_scanning'],
                'duration': 'hours_to_days',
                'detectability': 'medium'
            },
            'weaponization': {
                'indicators': ['malware_development', 'exploit_preparation', 'payload_creation'],
                'duration': 'days_to_weeks',
                'detectability': 'low'
            },
            'delivery': {
                'indicators': ['phishing_emails', 'malicious_attachments', 'drive_by_downloads'],
                'duration': 'minutes_to_hours',
                'detectability': 'high'
            },
            'exploitation': {
                'indicators': ['code_execution', 'privilege_escalation', 'system_compromise'],
                'duration': 'minutes_to_hours',
                'detectability': 'medium'
            },
            'installation': {
                'indicators': ['backdoor_installation', 'persistence_mechanism', 'malware_deployment'],
                'duration': 'minutes_to_hours',
                'detectability': 'medium'
            },
            'command_control': {
                'indicators': ['c2_communication', 'data_exfiltration', 'remote_control'],
                'duration': 'ongoing',
                'detectability': 'high'
            },
            'actions_on_objectives': {
                'indicators': ['data_theft', 'system_destruction', 'service_disruption'],
                'duration': 'hours_to_days',
                'detectability': 'high'
            }
        }
    
    def predict_attacks(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict potential attack scenarios"""
        attack_scenarios = []
        
        # Analyze current threat landscape
        threat_landscape = self._analyze_threat_landscape(entities, security_events)
        
        # Generate attack scenarios for each attack type
        for attack_type, attack_info in self.attack_types.items():
            scenarios = self._generate_attack_scenarios(
                attack_type, attack_info, entities, threat_landscape
            )
            attack_scenarios.extend(scenarios)
        
        # Rank scenarios by probability and impact
        attack_scenarios = self._rank_scenarios(attack_scenarios)
        
        return attack_scenarios
    
    def _analyze_threat_landscape(self, entities: Dict[str, Any], security_events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze current threat landscape"""
        landscape = {
            'vulnerability_density': self._calculate_vulnerability_density(entities),
            'threat_activity_level': self._calculate_threat_activity(security_events),
            'attack_surface': self._calculate_attack_surface(entities),
            'security_posture': self._assess_security_posture(entities),
            'recent_incidents': self._analyze_recent_incidents(security_events)
        }
        
        return landscape
    
    def _calculate_vulnerability_density(self, entities: Dict[str, Any]) -> float:
        """Calculate vulnerability density across entities"""
        total_vulnerabilities = 0
        total_entities = len(entities)
        
        for entity in entities.values():
            total_vulnerabilities += len(entity.get('vulnerabilities', []))
        
        return total_vulnerabilities / max(total_entities, 1)
    
    def _calculate_threat_activity(self, security_events: List[Dict[str, Any]]) -> float:
        """Calculate current threat activity level"""
        recent_events = [
            event for event in security_events
            if (datetime.now() - event['timestamp']).days <= 7
        ]
        
        # Weight events by severity
        activity_score = 0
        for event in recent_events:
            if event['type'] == 'vulnerability':
                severity = event['data'].get('severity', 'medium')
                weight = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}[severity]
                activity_score += weight
        
        return min(activity_score / 10.0, 1.0)  # Normalize to [0, 1]
    
    def _calculate_attack_surface(self, entities: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate attack surface metrics"""
        surface = {
            'total_entities': len(entities),
            'network_segments': set(),
            'open_ports': 0,
            'unencrypted_connections': 0,
            'critical_systems': 0
        }
        
        for entity in entities.values():
            surface['network_segments'].add(entity.get('network_segment', 'unknown'))
            
            connectivity = entity.get('connectivity', {})
            for connection in connectivity.get('connections', []):
                if not connection.get('encrypted', False):
                    surface['unencrypted_connections'] += 1
            
            if entity.get('criticality') == 'high':
                surface['critical_systems'] += 1
        
        surface['network_segments'] = len(surface['network_segments'])
        return surface
    
    def _assess_security_posture(self, entities: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall security posture"""
        posture = {
            'encryption_coverage': 0,
            'authentication_coverage': 0,
            'firewall_coverage': 0,
            'patch_management_coverage': 0
        }
        
        total_entities = len(entities)
        if total_entities == 0:
            return posture
        
        for entity in entities.values():
            security_config = entity.get('security_config', {})
            
            if security_config.get('encryption_enabled', False):
                posture['encryption_coverage'] += 1
            if security_config.get('authentication_required', False):
                posture['authentication_coverage'] += 1
            if security_config.get('firewall_enabled', False):
                posture['firewall_coverage'] += 1
            if security_config.get('patch_management') != 'none':
                posture['patch_management_coverage'] += 1
        
        # Convert to percentages
        for key in posture:
            posture[key] /= total_entities
        
        return posture
    
    def _analyze_recent_incidents(self, security_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyze recent security incidents"""
        recent_incidents = []
        
        for event in security_events[-20:]:  # Last 20 events
            if event['type'] in ['vulnerability', 'attack']:
                recent_incidents.append({
                    'type': event['type'],
                    'severity': event['data'].get('severity', 'medium'),
                    'timestamp': event['timestamp'],
                    'affected_system': event['data'].get('affected_system', 'unknown')
                })
        
        return recent_incidents
    
    def _generate_attack_scenarios(self, attack_type: str, attack_info: Dict[str, Any], 
                                 entities: Dict[str, Any], threat_landscape: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate attack scenarios for a specific attack type"""
        scenarios = []
        
        # Calculate base probability
        base_probability = attack_info['probability_base']
        
        # Adjust probability based on threat landscape
        adjusted_probability = self._adjust_probability(base_probability, threat_landscape, attack_type)
        
        # Generate scenarios for different threat actors
        for actor_type, actor_info in self.threat_actors.items():
            if self._is_compatible_target(attack_type, actor_info):
                scenario = self._create_attack_scenario(
                    attack_type, attack_info, actor_type, actor_info,
                    entities, adjusted_probability
                )
                scenarios.append(scenario)
        
        return scenarios
    
    def _adjust_probability(self, base_probability: float, threat_landscape: Dict[str, Any], 
                          attack_type: str) -> float:
        """Adjust attack probability based on current conditions"""
        adjusted = base_probability
        
        # Adjust based on vulnerability density
        vuln_density = threat_landscape['vulnerability_density']
        adjusted *= (1 + vuln_density * 0.5)
        
        # Adjust based on threat activity
        threat_activity = threat_landscape['threat_activity_level']
        adjusted *= (1 + threat_activity * 0.3)
        
        # Adjust based on attack surface
        attack_surface = threat_landscape['attack_surface']
        if attack_surface['unencrypted_connections'] > 0:
            adjusted *= 1.2
        
        # Adjust based on security posture
        security_posture = threat_landscape['security_posture']
        if security_posture['encryption_coverage'] < 0.5:
            adjusted *= 1.3
        if security_posture['authentication_coverage'] < 0.5:
            adjusted *= 1.4
        
        return min(adjusted, 1.0)  # Cap at 100%
    
    def _is_compatible_target(self, attack_type: str, actor_info: Dict[str, Any]) -> bool:
        """Check if attack type is compatible with threat actor"""
        target_preferences = actor_info['target_preference']
        attack_targets = self.attack_types[attack_type]['targets']
        
        return any(target in attack_targets for target in target_preferences)
    
    def _create_attack_scenario(self, attack_type: str, attack_info: Dict[str, Any],
                              actor_type: str, actor_info: Dict[str, Any],
                              entities: Dict[str, Any], probability: float) -> Dict[str, Any]:
        """Create a specific attack scenario"""
        # Select target entities
        target_entities = self._select_target_entities(attack_type, entities)
        
        # Generate attack path
        attack_path = self._generate_attack_path(attack_type, target_entities)
        
        # Calculate impact score
        impact_score = self._calculate_impact_score(attack_type, target_entities, actor_info)
        
        return {
            'id': f"{attack_type}_{actor_type}_{len(target_entities)}",
            'type': attack_type,
            'threat_actor': actor_type,
            'probability': probability,
            'severity': attack_info['severity'],
            'targets': target_entities,
            'attack_path': attack_path,
            'indicators': attack_info['indicators'],
            'impact_score': impact_score,
            'estimated_duration': self._estimate_attack_duration(attack_type),
            'detection_difficulty': self._assess_detection_difficulty(attack_type, actor_info),
            'mitigation_effort': self._assess_mitigation_effort(attack_type),
            'timestamp': datetime.now()
        }
    
    def _select_target_entities(self, attack_type: str, entities: Dict[str, Any]) -> List[str]:
        """Select target entities for the attack"""
        targets = []
        attack_targets = self.attack_types[attack_type]['targets']
        
        for entity_id, entity in entities.items():
            entity_type = entity['type']
            if any(target in entity_type for target in attack_targets):
                targets.append(entity_id)
        
        # Limit number of targets
        return targets[:min(len(targets), 5)]
    
    def _generate_attack_path(self, attack_type: str, target_entities: List[str]) -> List[str]:
        """Generate attack path to reach targets"""
        path = []
        
        # Add reconnaissance phase
        path.append('reconnaissance')
        
        # Add delivery mechanism
        if attack_type == 'ransomware':
            path.extend(['phishing', 'malware_delivery', 'execution'])
        elif attack_type == 'data_breach':
            path.extend(['initial_access', 'privilege_escalation', 'data_exfiltration'])
        elif attack_type == 'denial_of_service':
            path.extend(['traffic_generation', 'resource_exhaustion'])
        elif attack_type == 'medical_device_hijacking':
            path.extend(['device_discovery', 'vulnerability_exploitation', 'device_control'])
        
        # Add target compromise
        path.extend(['target_compromise'] + target_entities)
        
        return path
    
    def _calculate_impact_score(self, attack_type: str, target_entities: List[str], 
                              actor_info: Dict[str, Any]) -> float:
        """Calculate potential impact score"""
        base_impact = {'low': 0.3, 'medium': 0.6, 'high': 0.8, 'critical': 1.0}
        attack_severity = self.attack_types[attack_type]['severity']
        
        impact = base_impact[attack_severity]
        
        # Adjust based on actor capability
        capability_multiplier = {'low': 0.8, 'medium': 1.0, 'high': 1.3}
        impact *= capability_multiplier[actor_info['capability']]
        
        # Adjust based on number of targets
        impact *= min(len(target_entities) / 5.0, 1.0)
        
        return min(impact, 1.0)
    
    def _estimate_attack_duration(self, attack_type: str) -> str:
        """Estimate attack duration"""
        durations = {
            'ransomware': 'hours_to_days',
            'data_breach': 'days_to_weeks',
            'denial_of_service': 'minutes_to_hours',
            'insider_threat': 'weeks_to_months',
            'advanced_persistent_threat': 'months_to_years',
            'medical_device_hijacking': 'hours_to_days'
        }
        
        return durations.get(attack_type, 'unknown')
    
    def _assess_detection_difficulty(self, attack_type: str, actor_info: Dict[str, Any]) -> str:
        """Assess how difficult the attack is to detect"""
        if actor_info['capability'] == 'high':
            return 'difficult'
        elif attack_type in ['advanced_persistent_threat', 'insider_threat']:
            return 'difficult'
        else:
            return 'moderate'
    
    def _assess_mitigation_effort(self, attack_type: str) -> str:
        """Assess effort required to mitigate the attack"""
        if attack_type in ['advanced_persistent_threat', 'medical_device_hijacking']:
            return 'high'
        elif attack_type in ['ransomware', 'data_breach']:
            return 'medium'
        else:
            return 'low'
    
    def _rank_scenarios(self, scenarios: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Rank attack scenarios by risk score"""
        for scenario in scenarios:
            # Calculate risk score
            risk_score = scenario['probability'] * scenario['impact_score']
            scenario['risk_score'] = risk_score
        
        # Sort by risk score (descending)
        scenarios.sort(key=lambda x: x['risk_score'], reverse=True)
        
        return scenarios 