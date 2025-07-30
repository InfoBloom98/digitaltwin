"""
Anomaly Detection Model for Digital Twins
"""

import numpy as np
from typing import Dict, List, Any
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import os

class AnomalyDetector:
    """Machine learning-based anomaly detection for digital twins"""
    
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = StandardScaler()
        self.is_trained = False
        self.model_path = "models/anomaly_detector.pkl"
        self.scaler_path = "models/anomaly_scaler.pkl"
        
        # Load or initialize model
        self._load_or_initialize_model()
    
    def _load_or_initialize_model(self):
        """Load existing model or initialize new one"""
        try:
            if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
                self.model = joblib.load(self.model_path)
                self.scaler = joblib.load(self.scaler_path)
                self.is_trained = True
                print("Loaded existing anomaly detection model")
            else:
                self._initialize_model()
        except Exception as e:
            print(f"Error loading model: {e}")
            self._initialize_model()
    
    def _initialize_model(self):
        """Initialize new anomaly detection model"""
        model_config = self.config.get('models.anomaly_detection', {})
        
        self.model = IsolationForest(
            contamination=model_config.get('contamination', 0.1),
            n_estimators=model_config.get('n_estimators', 100),
            random_state=42
        )
        
        self.is_trained = False
        print("Initialized new anomaly detection model")
    
    def extract_features(self, entity: Dict[str, Any]) -> List[float]:
        """Extract numerical features from entity for anomaly detection"""
        features = []
        
        # Performance metrics
        metrics = entity.get('performance_metrics', {})
        features.extend([
            metrics.get('cpu_usage', 0),
            metrics.get('memory_usage', 0),
            metrics.get('network_usage', 0),
            metrics.get('disk_usage', 0),
            metrics.get('response_time', 0),
            metrics.get('error_rate', 0),
            metrics.get('uptime', 0)
        ])
        
        # Connectivity features
        connectivity = entity.get('connectivity', {})
        features.extend([
            len(connectivity.get('connections', [])),
            connectivity.get('total_bandwidth', 0),
            connectivity.get('network_latency', 0)
        ])
        
        # Security configuration features (binary)
        security_config = entity.get('security_config', {})
        features.extend([
            1.0 if security_config.get('encryption_enabled', False) else 0.0,
            1.0 if security_config.get('authentication_required', False) else 0.0,
            1.0 if security_config.get('firewall_enabled', False) else 0.0,
            1.0 if security_config.get('intrusion_detection', False) else 0.0,
            1.0 if security_config.get('audit_logging', False) else 0.0,
            1.0 if security_config.get('backup_enabled', False) else 0.0
        ])
        
        # Vulnerability count
        features.append(len(entity.get('vulnerabilities', [])))
        
        # Threat indicator count
        features.append(len(entity.get('threat_indicators', [])))
        
        # Entity type encoding
        entity_type = entity.get('type', 'unknown')
        type_encoding = {
            'medical_device': 1.0,
            'patient_monitor': 2.0,
            'hospital_server': 3.0,
            'network_device': 4.0,
            'database': 5.0
        }
        features.append(type_encoding.get(entity_type, 0.0))
        
        # Criticality encoding
        criticality = entity.get('criticality', 'low')
        criticality_encoding = {
            'low': 1.0,
            'medium': 2.0,
            'high': 3.0
        }
        features.append(criticality_encoding.get(criticality, 1.0))
        
        return features
    
    def train(self, entities: Dict[str, Any]):
        """Train the anomaly detection model"""
        if not entities:
            print("No entities provided for training")
            return
        
        # Extract features from all entities
        features_list = []
        for entity in entities.values():
            features = self.extract_features(entity)
            features_list.append(features)
        
        if not features_list:
            print("No features extracted for training")
            return
        
        # Convert to numpy array
        X = np.array(features_list)
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train model
        self.model.fit(X_scaled)
        self.is_trained = True
        
        # Save model
        self._save_model()
        
        print(f"Anomaly detection model trained on {len(entities)} entities")
    
    def detect_anomalies(self, entities: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Detect anomalies in entities"""
        if not self.is_trained:
            print("Model not trained. Training on current data...")
            self.train(entities)
        
        anomalies = []
        
        for entity_id, entity in entities.items():
            # Extract features
            features = self.extract_features(entity)
            X = np.array([features])
            
            # Scale features
            X_scaled = self.scaler.transform(X)
            
            # Predict anomaly
            prediction = self.model.predict(X_scaled)[0]
            score = self.model.decision_function(X_scaled)[0]
            
            # -1 indicates anomaly, 1 indicates normal
            if prediction == -1:
                anomaly = {
                    'entity_id': entity_id,
                    'entity_name': entity.get('name', 'Unknown'),
                    'anomaly_score': abs(score),
                    'severity': self._determine_anomaly_severity(abs(score)),
                    'features': features,
                    'description': self._generate_anomaly_description(entity, abs(score)),
                    'timestamp': entity.get('last_updated', None)
                }
                anomalies.append(anomaly)
        
        return anomalies
    
    def _determine_anomaly_severity(self, score: float) -> str:
        """Determine anomaly severity based on score"""
        if score > 0.8:
            return 'critical'
        elif score > 0.6:
            return 'high'
        elif score > 0.4:
            return 'medium'
        else:
            return 'low'
    
    def _generate_anomaly_description(self, entity: Dict[str, Any], score: float) -> str:
        """Generate description for detected anomaly"""
        entity_type = entity.get('type', 'unknown')
        metrics = entity.get('performance_metrics', {})
        
        descriptions = []
        
        # Check for performance anomalies
        if metrics.get('cpu_usage', 0) > 90:
            descriptions.append("Unusually high CPU usage")
        if metrics.get('memory_usage', 0) > 95:
            descriptions.append("Unusually high memory usage")
        if metrics.get('error_rate', 0) > 0.1:
            descriptions.append("High error rate")
        
        # Check for security anomalies
        security_config = entity.get('security_config', {})
        if not security_config.get('encryption_enabled', False):
            descriptions.append("Encryption disabled")
        if not security_config.get('authentication_required', False):
            descriptions.append("No authentication required")
        
        # Check for connectivity anomalies
        connectivity = entity.get('connectivity', {})
        if len(connectivity.get('connections', [])) > 10:
            descriptions.append("Unusually high number of connections")
        
        if descriptions:
            return f"Anomaly detected in {entity_type}: {'; '.join(descriptions)}"
        else:
            return f"Statistical anomaly detected in {entity_type} (score: {score:.3f})"
    
    def _save_model(self):
        """Save the trained model"""
        try:
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            joblib.dump(self.model, self.model_path)
            joblib.dump(self.scaler, self.scaler_path)
            print("Model saved successfully")
        except Exception as e:
            print(f"Error saving model: {e}")
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model"""
        return {
            'is_trained': self.is_trained,
            'model_type': 'IsolationForest',
            'contamination': self.model.contamination if self.model else None,
            'n_estimators': self.model.n_estimators if self.model else None,
            'model_path': self.model_path,
            'scaler_path': self.scaler_path
        }
    
    def update_model(self, new_entities: Dict[str, Any]):
        """Update model with new data"""
        if not self.is_trained:
            self.train(new_entities)
            return
        
        # Extract features from new entities
        features_list = []
        for entity in new_entities.values():
            features = self.extract_features(entity)
            features_list.append(features)
        
        if not features_list:
            return
        
        # Convert to numpy array
        X = np.array(features_list)
        
        # Scale features using existing scaler
        X_scaled = self.scaler.transform(X)
        
        # Update model (partial fit if supported)
        if hasattr(self.model, 'partial_fit'):
            self.model.partial_fit(X_scaled)
        else:
            # Retrain with combined data
            print("Partial fit not supported, retraining model...")
            self.train(new_entities)
        
        # Save updated model
        self._save_model()
        
        print(f"Model updated with {len(new_entities)} new entities") 