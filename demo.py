#!/usr/bin/env python3
"""
Demo script for Digital Twin Cybersecurity Simulation
"""

import sys
import time
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

from utils.config import Config
from utils.logger import setup_logger
from data.digital_twin_generator import DigitalTwinGenerator
from security.vulnerability_detector import VulnerabilityDetector
from security.attack_predictor import AttackPredictor
from security.security_evaluator import SecurityEvaluator
from security.resilience_enhancer import ResilienceEnhancer
from models.anomaly_detector import AnomalyDetector

def main():
    """Run the cybersecurity simulation demo"""
    print("🔒 Digital Twin Cybersecurity Simulation Demo")
    print("=" * 50)
    
    # Setup logging
    logger = setup_logger()
    logger.info("Starting cybersecurity simulation demo")
    
    # Load configuration
    config = Config()
    print("✅ Configuration loaded")
    
    # Initialize components
    print("\n🚀 Initializing simulation components...")
    
    generator = DigitalTwinGenerator(config)
    detector = VulnerabilityDetector(config)
    predictor = AttackPredictor(config)
    evaluator = SecurityEvaluator(config)
    enhancer = ResilienceEnhancer(config)
    anomaly_detector = AnomalyDetector(config)
    
    print("✅ All components initialized")
    
    # Generate digital twins
    print("\n🏥 Generating digital twin entities...")
    entities = generator.generate_entities(50)
    entities_dict = {entity['id']: entity for entity in entities}
    
    print(f"✅ Generated {len(entities)} digital twin entities")
    print(f"   - Medical devices: {len([e for e in entities if e['type'] == 'medical_device'])}")
    print(f"   - Patient monitors: {len([e for e in entities if e['type'] == 'patient_monitor'])}")
    print(f"   - Hospital servers: {len([e for e in entities if e['type'] == 'hospital_server'])}")
    print(f"   - Network devices: {len([e for e in entities if e['type'] == 'network_device'])}")
    print(f"   - Databases: {len([e for e in entities if e['type'] == 'database'])}")
    
    # Detect vulnerabilities
    print("\n🔍 Detecting vulnerabilities...")
    vulnerabilities = detector.detect_vulnerabilities(entities_dict)
    
    print(f"✅ Detected {len(vulnerabilities)} vulnerabilities")
    severity_counts = {}
    for vuln in vulnerabilities:
        severity = vuln['severity']
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
    for severity, count in severity_counts.items():
        print(f"   - {severity.capitalize()}: {count}")
    
    # Predict attacks
    print("\n🎯 Predicting attack scenarios...")
    attack_scenarios = predictor.predict_attacks(entities_dict, [])
    
    print(f"✅ Predicted {len(attack_scenarios)} attack scenarios")
    attack_types = {}
    for scenario in attack_scenarios:
        attack_type = scenario['type']
        attack_types[attack_type] = attack_types.get(attack_type, 0) + 1
    
    for attack_type, count in attack_types.items():
        print(f"   - {attack_type.replace('_', ' ').title()}: {count}")
    
    # Evaluate security posture
    print("\n📊 Evaluating security posture...")
    security_score = evaluator.evaluate_security(entities_dict, [])
    
    print(f"✅ Security score: {security_score:.1f}/100")
    
    if security_score >= 80:
        print("   🟢 Excellent security posture")
    elif security_score >= 60:
        print("   🟡 Good security posture")
    elif security_score >= 40:
        print("   🟠 Fair security posture")
    else:
        print("   🔴 Poor security posture - immediate action required")
    
    # Generate recommendations
    print("\n💡 Generating security recommendations...")
    recommendations = enhancer.generate_recommendations(entities_dict, [], {'security_score': security_score})
    
    print(f"✅ Generated {len(recommendations)} recommendations")
    
    # Show top recommendations
    high_priority = [r for r in recommendations if r['priority'] == 'high']
    if high_priority:
        print("\n🔴 High Priority Recommendations:")
        for i, rec in enumerate(high_priority[:3], 1):
            print(f"   {i}. {rec['title']}")
            print(f"      {rec['description']}")
            print()
    
    # Detect anomalies
    print("\n🚨 Detecting anomalies...")
    anomaly_detector.train(entities_dict)
    anomalies = anomaly_detector.detect_anomalies(entities_dict)
    
    print(f"✅ Detected {len(anomalies)} anomalies")
    if anomalies:
        print("\n🔍 Top Anomalies:")
        for i, anomaly in enumerate(anomalies[:3], 1):
            print(f"   {i}. {anomaly['entity_name']} - {anomaly['severity']} severity")
            print(f"      Score: {anomaly['anomaly_score']:.3f}")
            print(f"      {anomaly['description']}")
            print()
    
    # Simulate security improvements
    print("\n🔄 Simulating security improvements...")
    
    # Apply some recommendations
    applied_count = 0
    for rec in recommendations[:5]:  # Apply first 5 recommendations
        if enhancer.apply_recommendation(rec, entities_dict):
            applied_count += 1
    
    print(f"✅ Applied {applied_count} security improvements")
    
    # Re-evaluate security
    new_security_score = evaluator.evaluate_security(entities_dict, [])
    improvement = new_security_score - security_score
    
    print(f"✅ New security score: {new_security_score:.1f}/100")
    print(f"   📈 Improvement: {improvement:+.1f} points")
    
    # Generate improvement plan
    print("\n📋 Generating comprehensive improvement plan...")
    improvement_plan = enhancer.generate_improvement_plan(entities_dict, [], {'security_score': new_security_score})
    
    print("✅ Improvement plan generated")
    print(f"   - Current state: {improvement_plan['current_state']['security_score']:.1f}/100")
    print(f"   - Expected improvements: +{improvement_plan['expected_improvements']['security_score_increase']:.1f} points")
    print(f"   - Timeline phases: {len(improvement_plan['timeline'])}")
    
    # Final summary
    print("\n" + "=" * 50)
    print("📊 DEMO SUMMARY")
    print("=" * 50)
    print(f"🏥 Digital Twins: {len(entities)} entities")
    print(f"🔍 Vulnerabilities: {len(vulnerabilities)} detected")
    print(f"🎯 Attack Scenarios: {len(attack_scenarios)} predicted")
    print(f"📊 Security Score: {security_score:.1f} → {new_security_score:.1f}")
    print(f"🚨 Anomalies: {len(anomalies)} detected")
    print(f"💡 Recommendations: {len(recommendations)} generated")
    print(f"✅ Improvements: {applied_count} applied")
    
    print("\n🎉 Demo completed successfully!")
    print("\nTo run the full simulation with web dashboard:")
    print("   python src/main.py")
    print("\nTo run tests:")
    print("   python -m pytest tests/")
    
    logger.info("Demo completed successfully")

if __name__ == "__main__":
    main() 