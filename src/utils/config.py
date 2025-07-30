"""
Configuration management for the cybersecurity simulation
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any

class Config:
    """Configuration manager for the simulation"""
    
    def __init__(self, config_path: str = None):
        self.config_path = config_path or "config/simulation_config.yaml"
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            config_file = Path(self.config_path)
            if config_file.exists():
                with open(config_file, 'r') as f:
                    return yaml.safe_load(f)
            else:
                return self._get_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            'simulation': {
                'duration': 3600,  # seconds
                'update_interval': 1,  # seconds
                'max_entities': 1000
            },
            'security': {
                'vulnerability_scan_interval': 300,  # seconds
                'threat_detection_sensitivity': 0.8,
                'max_false_positive_rate': 0.02,
                'response_time_threshold': 100  # milliseconds
            },
            'models': {
                'anomaly_detection': {
                    'algorithm': 'isolation_forest',
                    'contamination': 0.1,
                    'n_estimators': 100
                },
                'attack_prediction': {
                    'algorithm': 'random_forest',
                    'n_estimators': 200,
                    'max_depth': 10
                },
                'vulnerability_assessment': {
                    'algorithm': 'gradient_boosting',
                    'learning_rate': 0.1,
                    'n_estimators': 100
                }
            },
            'dashboard': {
                'host': 'localhost',
                'port': 5000,
                'debug': False,
                'auto_reload': True
            },
            'data': {
                'input_path': 'data/input/',
                'output_path': 'data/output/',
                'backup_path': 'data/backup/',
                'max_file_size': 100 * 1024 * 1024  # 100MB
            },
            'logging': {
                'level': 'INFO',
                'file': 'logs/simulation.log',
                'max_size': 10 * 1024 * 1024,  # 10MB
                'backup_count': 5
            }
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value by key"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def save(self) -> None:
        """Save configuration to file"""
        try:
            config_file = Path(self.config_path)
            config_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(config_file, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def validate(self) -> bool:
        """Validate configuration"""
        required_keys = [
            'simulation.duration',
            'simulation.update_interval',
            'security.vulnerability_scan_interval',
            'dashboard.host',
            'dashboard.port'
        ]
        
        for key in required_keys:
            if self.get(key) is None:
                print(f"Missing required configuration: {key}")
                return False
        
        return True 