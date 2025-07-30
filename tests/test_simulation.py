"""
Unit tests for the cybersecurity simulation
"""

import unittest
import sys
import os
from unittest.mock import Mock, patch
import tempfile
import shutil

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.config import Config
from data.digital_twin_generator import DigitalTwinGenerator
from security.vulnerability_detector import VulnerabilityDetector
from security.attack_predictor import AttackPredictor
from security.security_evaluator import SecurityEvaluator
from security.resilience_enhancer import ResilienceEnhancer
from models.anomaly_detector import AnomalyDetector

class TestConfig(unittest.TestCase):
    """Test configuration management"""
    
    def setUp(self):
        self.config = Config()
    
    def test_default_config(self):
        """Test default configuration loading"""
        self.assertIsNotNone(self.config.get('simulation.duration'))
        self.assertIsNotNone(self.config.get('dashboard.port'))
        self.assertEqual(self.config.get('dashboard.port'), 5000)
    
    def test_config_set_get(self):
        """Test setting and getting configuration values"""
        self.config.set('test.value', 123)
        self.assertEqual(self.config.get('test.value'), 123)
    
    def test_config_validation(self):
        """Test configuration validation"""
        self.assertTrue(self.config.validate())

class TestDigitalTwinGenerator(unittest.TestCase):
    """Test digital twin generator"""
    
    def setUp(self):
        self.config = Config()
        self.generator = DigitalTwinGenerator(self.config)
    
    def test_generate_entities(self):
        """Test entity generation"""
        entities = self.generator.generate_entities(5)
        self.assertEqual(len(entities), 5)
        
        for entity in entities:
            self.assertIn('id', entity)
            self.assertIn('type', entity)
            self.assertIn('name', entity)
            self.assertIn('security_config', entity)
    
    def test_entity_types(self):
        """Test entity type distribution"""
        entities = self.generator.generate_entities(100)
        types = [entity['type'] for entity in entities]
        
        # Should have multiple entity types
        self.assertGreater(len(set(types)), 1)
        
        # All types should be valid
        valid_types = ['medical_device', 'patient_monitor', 'hospital_server', 'network_device', 'database']
        for entity_type in types:
            self.assertIn(entity_type, valid_types)
    
    def test_update_entity(self):
        """Test entity updating"""
        entities = self.generator.generate_entities(1)
        original_entity = entities[0]
        
        updated_entity = self.generator.update_entity(original_entity)
        
        self.assertNotEqual(original_entity['last_updated'], updated_entity['last_updated'])
        self.assertIn('performance_metrics', updated_entity)

class TestVulnerabilityDetector(unittest.TestCase):
    """Test vulnerability detection"""
    
    def setUp(self):
        self.config = Config()
        self.detector = VulnerabilityDetector(self.config)
        self.generator = DigitalTwinGenerator(self.config)
    
    def test_detect_vulnerabilities(self):
        """Test vulnerability detection"""
        entities = self.generator.generate_entities(10)
        entities_dict = {entity['id']: entity for entity in entities}
        
        vulnerabilities = self.detector.detect_vulnerabilities(entities_dict)
        
        # Should return a list
        self.assertIsInstance(vulnerabilities, list)
        
        # Each vulnerability should have required fields
        for vuln in vulnerabilities:
            self.assertIn('type', vuln)
            self.assertIn('severity', vuln)
            self.assertIn('description', vuln)
            self.assertIn('affected_system', vuln)
    
    def test_security_config_check(self):
        """Test security configuration checking"""
        entity = {
            'id': 'test',
            'name': 'Test Entity',
            'security_config': {
                'encryption_enabled': False,
                'authentication_required': False,
                'firewall_enabled': False
            }
        }
        
        vulnerabilities = self.detector._check_security_config(entity)
        
        # Should detect multiple vulnerabilities
        self.assertGreater(len(vulnerabilities), 0)
        
        # Should detect encryption vulnerability
        vuln_types = [v['type'] for v in vulnerabilities]
        self.assertIn('encryption_disabled', vuln_types)

class TestAttackPredictor(unittest.TestCase):
    """Test attack prediction"""
    
    def setUp(self):
        self.config = Config()
        self.predictor = AttackPredictor(self.config)
        self.generator = DigitalTwinGenerator(self.config)
    
    def test_predict_attacks(self):
        """Test attack prediction"""
        entities = self.generator.generate_entities(10)
        entities_dict = {entity['id']: entity for entity in entities}
        security_events = []
        
        attack_scenarios = self.predictor.predict_attacks(entities_dict, security_events)
        
        # Should return a list
        self.assertIsInstance(attack_scenarios, list)
        
        # Each scenario should have required fields
        for scenario in attack_scenarios:
            self.assertIn('type', scenario)
            self.assertIn('probability', scenario)
            self.assertIn('severity', scenario)
            self.assertIn('targets', scenario)
    
    def test_threat_landscape_analysis(self):
        """Test threat landscape analysis"""
        entities = self.generator.generate_entities(5)
        entities_dict = {entity['id']: entity for entity in entities}
        security_events = []
        
        landscape = self.predictor._analyze_threat_landscape(entities_dict, security_events)
        
        # Should have required fields
        self.assertIn('vulnerability_density', landscape)
        self.assertIn('threat_activity_level', landscape)
        self.assertIn('attack_surface', landscape)
        self.assertIn('security_posture', landscape)

class TestSecurityEvaluator(unittest.TestCase):
    """Test security evaluation"""
    
    def setUp(self):
        self.config = Config()
        self.evaluator = SecurityEvaluator(self.config)
        self.generator = DigitalTwinGenerator(self.config)
    
    def test_evaluate_security(self):
        """Test security evaluation"""
        entities = self.generator.generate_entities(10)
        entities_dict = {entity['id']: entity for entity in entities}
        security_events = []
        
        security_score = self.evaluator.evaluate_security(entities_dict, security_events)
        
        # Should return a score between 0 and 100
        self.assertIsInstance(security_score, float)
        self.assertGreaterEqual(security_score, 0)
        self.assertLessEqual(security_score, 100)
    
    def test_access_control_assessment(self):
        """Test access control assessment"""
        entities = self.generator.generate_entities(5)
        entities_dict = {entity['id']: entity for entity in entities}
        
        auth_strength = self.evaluator._assess_authentication_strength(entities_dict)
        
        # Should return a percentage
        self.assertIsInstance(auth_strength, float)
        self.assertGreaterEqual(auth_strength, 0)
        self.assertLessEqual(auth_strength, 100)

class TestResilienceEnhancer(unittest.TestCase):
    """Test resilience enhancement"""
    
    def setUp(self):
        self.config = Config()
        self.enhancer = ResilienceEnhancer(self.config)
        self.generator = DigitalTwinGenerator(self.config)
    
    def test_generate_recommendations(self):
        """Test recommendation generation"""
        entities = self.generator.generate_entities(10)
        entities_dict = {entity['id']: entity for entity in entities}
        security_events = []
        metrics = {'security_score': 50}
        
        recommendations = self.enhancer.generate_recommendations(entities_dict, security_events, metrics)
        
        # Should return a list
        self.assertIsInstance(recommendations, list)
        
        # Each recommendation should have required fields
        for rec in recommendations:
            self.assertIn('id', rec)
            self.assertIn('title', rec)
            self.assertIn('description', rec)
            self.assertIn('priority', rec)
            self.assertIn('effort', rec)
            self.assertIn('impact', rec)
    
    def test_apply_recommendation(self):
        """Test recommendation application"""
        entities = self.generator.generate_entities(1)
        entities_dict = {entities[0]['id']: entities[0]}
        
        # Create a test recommendation
        recommendation = {
            'id': 'test_rec',
            'type': 'encryption',
            'target_entity': entities[0]['id']
        }
        
        success = self.enhancer.apply_recommendation(recommendation, entities_dict)
        
        # Should return boolean
        self.assertIsInstance(success, bool)

class TestAnomalyDetector(unittest.TestCase):
    """Test anomaly detection"""
    
    def setUp(self):
        self.config = Config()
        self.detector = AnomalyDetector(self.config)
        self.generator = DigitalTwinGenerator(self.config)
    
    def test_feature_extraction(self):
        """Test feature extraction"""
        entities = self.generator.generate_entities(1)
        entity = entities[0]
        
        features = self.detector.extract_features(entity)
        
        # Should return a list of numerical features
        self.assertIsInstance(features, list)
        self.assertGreater(len(features), 0)
        
        # All features should be numbers
        for feature in features:
            self.assertIsInstance(feature, (int, float))
    
    def test_anomaly_detection(self):
        """Test anomaly detection"""
        entities = self.generator.generate_entities(10)
        entities_dict = {entity['id']: entity for entity in entities}
        
        # Train the model
        self.detector.train(entities_dict)
        
        # Detect anomalies
        anomalies = self.detector.detect_anomalies(entities_dict)
        
        # Should return a list
        self.assertIsInstance(anomalies, list)
        
        # Each anomaly should have required fields
        for anomaly in anomalies:
            self.assertIn('entity_id', anomaly)
            self.assertIn('anomaly_score', anomaly)
            self.assertIn('severity', anomaly)
            self.assertIn('description', anomaly)

class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def setUp(self):
        self.config = Config()
        self.generator = DigitalTwinGenerator(self.config)
        self.detector = VulnerabilityDetector(self.config)
        self.predictor = AttackPredictor(self.config)
        self.evaluator = SecurityEvaluator(self.config)
        self.enhancer = ResilienceEnhancer(self.config)
        self.anomaly_detector = AnomalyDetector(self.config)
    
    def test_full_workflow(self):
        """Test complete workflow"""
        # Generate entities
        entities = self.generator.generate_entities(20)
        entities_dict = {entity['id']: entity for entity in entities}
        
        # Detect vulnerabilities
        vulnerabilities = self.detector.detect_vulnerabilities(entities_dict)
        
        # Predict attacks
        attack_scenarios = self.predictor.predict_attacks(entities_dict, [])
        
        # Evaluate security
        security_score = self.evaluator.evaluate_security(entities_dict, [])
        
        # Generate recommendations
        recommendations = self.enhancer.generate_recommendations(entities_dict, [], {'security_score': security_score})
        
        # Detect anomalies
        self.anomaly_detector.train(entities_dict)
        anomalies = self.anomaly_detector.detect_anomalies(entities_dict)
        
        # All components should work together
        self.assertIsInstance(vulnerabilities, list)
        self.assertIsInstance(attack_scenarios, list)
        self.assertIsInstance(security_score, float)
        self.assertIsInstance(recommendations, list)
        self.assertIsInstance(anomalies, list)

if __name__ == '__main__':
    unittest.main() 