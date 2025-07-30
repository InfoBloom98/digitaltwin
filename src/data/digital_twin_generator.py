"""
Digital Twin Generator for Healthcare Infrastructure
"""

import uuid
import random
import numpy as np
from typing import Dict, List, Any
from datetime import datetime, timedelta

class DigitalTwinGenerator:
    """Generates and manages digital twin entities for healthcare infrastructure"""
    
    def __init__(self, config):
        self.config = config
        self.entity_types = {
            'medical_device': {
                'weight': 0.3,
                'vulnerabilities': ['firmware_outdated', 'default_credentials', 'unencrypted_communication'],
                'criticality': ['high', 'medium', 'low']
            },
            'patient_monitor': {
                'weight': 0.25,
                'vulnerabilities': ['weak_authentication', 'data_exposure', 'network_isolation'],
                'criticality': ['high', 'high', 'medium']
            },
            'hospital_server': {
                'weight': 0.2,
                'vulnerabilities': ['unpatched_system', 'privilege_escalation', 'sql_injection'],
                'criticality': ['high', 'medium', 'medium']
            },
            'network_device': {
                'weight': 0.15,
                'vulnerabilities': ['misconfiguration', 'weak_encryption', 'backdoor_access'],
                'criticality': ['medium', 'medium', 'low']
            },
            'database': {
                'weight': 0.1,
                'vulnerabilities': ['weak_passwords', 'unencrypted_data', 'injection_attacks'],
                'criticality': ['high', 'high', 'medium']
            }
        }
        
        self.network_segments = [
            'patient_care_network',
            'administrative_network', 
            'research_network',
            'emergency_network',
            'isolation_network'
        ]
        
        self.security_levels = ['low', 'medium', 'high', 'critical']
        
    def generate_entities(self, count: int) -> List[Dict[str, Any]]:
        """Generate a specified number of digital twin entities"""
        entities = []
        
        for _ in range(count):
            entity_type = self._select_entity_type()
            entity = self._create_entity(entity_type)
            entities.append(entity)
        
        return entities
    
    def _select_entity_type(self) -> str:
        """Select entity type based on weights"""
        weights = [self.entity_types[et]['weight'] for et in self.entity_types.keys()]
        return random.choices(list(self.entity_types.keys()), weights=weights)[0]
    
    def _create_entity(self, entity_type: str) -> Dict[str, Any]:
        """Create a single digital twin entity"""
        entity = {
            'id': str(uuid.uuid4()),
            'type': entity_type,
            'name': self._generate_name(entity_type),
            'network_segment': random.choice(self.network_segments),
            'security_level': random.choice(self.security_levels),
            'criticality': random.choice(self.entity_types[entity_type]['criticality']),
            'created_at': datetime.now(),
            'last_updated': datetime.now(),
            'status': 'active',
            'location': self._generate_location(),
            'specifications': self._generate_specifications(entity_type),
            'security_config': self._generate_security_config(entity_type),
            'vulnerabilities': [],
            'threat_indicators': [],
            'performance_metrics': self._generate_performance_metrics(),
            'connectivity': self._generate_connectivity(entity_type)
        }
        
        return entity
    
    def _generate_name(self, entity_type: str) -> str:
        """Generate realistic entity names"""
        prefixes = {
            'medical_device': ['MRI', 'CT', 'X-Ray', 'Ultrasound', 'ECG'],
            'patient_monitor': ['Monitor', 'VitalSigns', 'PatientCare', 'ICU', 'ER'],
            'hospital_server': ['Server', 'MainFrame', 'DataCenter', 'Backup', 'Archive'],
            'network_device': ['Router', 'Switch', 'Firewall', 'Gateway', 'Hub'],
            'database': ['PatientDB', 'MedicalDB', 'AdminDB', 'ResearchDB', 'ArchiveDB']
        }
        
        prefix = random.choice(prefixes[entity_type])
        suffix = f"-{random.randint(1000, 9999)}"
        return f"{prefix}{suffix}"
    
    def _generate_location(self) -> Dict[str, Any]:
        """Generate entity location information"""
        buildings = ['Main', 'North', 'South', 'East', 'West', 'Emergency', 'Research']
        floors = list(range(1, 11))
        rooms = list(range(100, 999))
        
        return {
            'building': random.choice(buildings),
            'floor': random.choice(floors),
            'room': random.choice(rooms),
            'coordinates': {
                'x': random.uniform(0, 1000),
                'y': random.uniform(0, 1000),
                'z': random.uniform(0, 100)
            }
        }
    
    def _generate_specifications(self, entity_type: str) -> Dict[str, Any]:
        """Generate entity specifications"""
        specs = {
            'manufacturer': random.choice(['Siemens', 'GE', 'Philips', 'Cisco', 'Dell', 'HP']),
            'model': f"Model-{random.randint(100, 999)}",
            'version': f"{random.randint(1, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)}",
            'firmware_version': f"FW-{random.randint(1, 5)}.{random.randint(0, 9)}",
            'operating_system': random.choice(['Linux', 'Windows', 'Embedded', 'Custom']),
            'memory': f"{random.choice([4, 8, 16, 32, 64])}GB",
            'storage': f"{random.choice([100, 500, 1000, 2000])}GB",
            'network_ports': random.randint(1, 8)
        }
        
        return specs
    
    def _generate_security_config(self, entity_type: str) -> Dict[str, Any]:
        """Generate security configuration"""
        config = {
            'encryption_enabled': random.choice([True, False]),
            'authentication_required': random.choice([True, False]),
            'firewall_enabled': random.choice([True, False]),
            'intrusion_detection': random.choice([True, False]),
            'access_control': random.choice(['role_based', 'attribute_based', 'none']),
            'audit_logging': random.choice([True, False]),
            'backup_enabled': random.choice([True, False]),
            'patch_management': random.choice(['automatic', 'manual', 'none']),
            'vulnerability_scanning': random.choice([True, False]),
            'network_isolation': random.choice([True, False])
        }
        
        return config
    
    def _generate_performance_metrics(self) -> Dict[str, Any]:
        """Generate performance metrics"""
        return {
            'cpu_usage': random.uniform(10, 90),
            'memory_usage': random.uniform(20, 85),
            'network_usage': random.uniform(5, 80),
            'disk_usage': random.uniform(15, 95),
            'response_time': random.uniform(10, 500),
            'uptime': random.uniform(0.8, 0.999),
            'error_rate': random.uniform(0, 0.05)
        }
    
    def _generate_connectivity(self, entity_type: str) -> Dict[str, Any]:
        """Generate connectivity information"""
        connections = []
        num_connections = random.randint(1, 5)
        
        for _ in range(num_connections):
            connection = {
                'target_id': str(uuid.uuid4()),
                'protocol': random.choice(['TCP', 'UDP', 'HTTP', 'HTTPS', 'FTP', 'SSH']),
                'port': random.randint(1, 65535),
                'encrypted': random.choice([True, False]),
                'bandwidth': random.uniform(10, 1000)
            }
            connections.append(connection)
        
        return {
            'connections': connections,
            'total_bandwidth': sum(c['bandwidth'] for c in connections),
            'network_latency': random.uniform(1, 100)
        }
    
    def update_entity(self, entity: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing entity with new data"""
        # Update performance metrics
        entity['performance_metrics'] = self._update_performance_metrics(
            entity['performance_metrics']
        )
        
        # Update connectivity
        entity['connectivity'] = self._update_connectivity(entity['connectivity'])
        
        # Update timestamp
        entity['last_updated'] = datetime.now()
        
        # Randomly add new vulnerabilities
        if random.random() < 0.01:  # 1% chance
            new_vuln = self._generate_vulnerability(entity['type'])
            entity['vulnerabilities'].append(new_vuln)
        
        # Randomly add threat indicators
        if random.random() < 0.005:  # 0.5% chance
            new_threat = self._generate_threat_indicator()
            entity['threat_indicators'].append(new_threat)
        
        return entity
    
    def _update_performance_metrics(self, current_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Update performance metrics with realistic variations"""
        updated_metrics = {}
        
        for key, value in current_metrics.items():
            if isinstance(value, float):
                # Add realistic variation (±10%)
                variation = random.uniform(-0.1, 0.1)
                new_value = value * (1 + variation)
                
                # Ensure values stay within reasonable bounds
                if 'usage' in key:
                    new_value = max(0, min(100, new_value))
                elif 'rate' in key:
                    new_value = max(0, min(1, new_value))
                elif 'time' in key:
                    new_value = max(0, new_value)
                elif 'uptime' in key:
                    new_value = max(0, min(1, new_value))
                
                updated_metrics[key] = new_value
            else:
                updated_metrics[key] = value
        
        return updated_metrics
    
    def _update_connectivity(self, current_connectivity: Dict[str, Any]) -> Dict[str, Any]:
        """Update connectivity information"""
        # Update network latency
        current_connectivity['network_latency'] = max(0, 
            current_connectivity['network_latency'] + random.uniform(-5, 5)
        )
        
        # Update bandwidth for each connection
        for connection in current_connectivity['connections']:
            connection['bandwidth'] = max(0, 
                connection['bandwidth'] + random.uniform(-10, 10)
            )
        
        # Recalculate total bandwidth
        current_connectivity['total_bandwidth'] = sum(
            c['bandwidth'] for c in current_connectivity['connections']
        )
        
        return current_connectivity
    
    def _generate_vulnerability(self, entity_type: str) -> Dict[str, Any]:
        """Generate a new vulnerability"""
        vuln_types = self.entity_types[entity_type]['vulnerabilities']
        vuln_type = random.choice(vuln_types)
        
        return {
            'id': str(uuid.uuid4()),
            'type': vuln_type,
            'severity': random.choice(['low', 'medium', 'high', 'critical']),
            'description': f"Generated {vuln_type} vulnerability",
            'discovered_at': datetime.now(),
            'status': 'open',
            'cvss_score': random.uniform(1, 10),
            'exploitability': random.choice(['easy', 'medium', 'hard', 'theoretical'])
        }
    
    def _generate_threat_indicator(self) -> Dict[str, Any]:
        """Generate a threat indicator"""
        indicator_types = [
            'suspicious_network_activity',
            'unusual_login_attempts',
            'data_exfiltration',
            'malware_detection',
            'privilege_escalation',
            'denial_of_service'
        ]
        
        return {
            'id': str(uuid.uuid4()),
            'type': random.choice(indicator_types),
            'confidence': random.uniform(0.1, 1.0),
            'severity': random.choice(['low', 'medium', 'high', 'critical']),
            'detected_at': datetime.now(),
            'source_ip': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
            'description': f"Detected {indicator_types[0]} activity"
        } 