"""
Logging configuration for the cybersecurity simulation
"""

import logging
import logging.handlers
import os
from pathlib import Path
from datetime import datetime

def setup_logger(name: str = "cybersecurity_simulation", 
                level: str = "INFO",
                log_file: str = "logs/simulation.log") -> logging.Logger:
    """
    Setup and configure logger for the simulation
    
    Args:
        name: Logger name
        level: Logging level
        log_file: Path to log file
        
    Returns:
        Configured logger instance
    """
    
    # Create logs directory if it doesn't exist
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Clear existing handlers
    logger.handlers.clear()
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s'
    )
    
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    logger.addHandler(file_handler)
    
    # Security events handler
    security_log_file = "logs/security_events.log"
    security_handler = logging.handlers.RotatingFileHandler(
        security_log_file,
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    security_handler.setLevel(logging.WARNING)
    security_handler.setFormatter(detailed_formatter)
    
    # Create security logger
    security_logger = logging.getLogger(f"{name}.security")
    security_logger.addHandler(security_handler)
    security_logger.setLevel(logging.WARNING)
    
    return logger

class SecurityLogger:
    """Specialized logger for security events"""
    
    def __init__(self, logger_name: str = "security"):
        self.logger = logging.getLogger(f"cybersecurity_simulation.{logger_name}")
    
    def log_vulnerability(self, vulnerability_type: str, severity: str, 
                         description: str, affected_system: str):
        """Log vulnerability detection"""
        self.logger.warning(
            f"VULNERABILITY DETECTED - Type: {vulnerability_type}, "
            f"Severity: {severity}, System: {affected_system}, "
            f"Description: {description}"
        )
    
    def log_attack(self, attack_type: str, source: str, target: str, 
                   success: bool, details: str):
        """Log attack attempt"""
        status = "SUCCESSFUL" if success else "BLOCKED"
        self.logger.warning(
            f"ATTACK {status} - Type: {attack_type}, "
            f"Source: {source}, Target: {target}, Details: {details}"
        )
    
    def log_incident(self, incident_type: str, severity: str, 
                     description: str, response_time: float):
        """Log security incident"""
        self.logger.error(
            f"SECURITY INCIDENT - Type: {incident_type}, "
            f"Severity: {severity}, Response Time: {response_time}ms, "
            f"Description: {description}"
        )
    
    def log_threat_intelligence(self, threat_type: str, confidence: float, 
                               source: str, indicators: list):
        """Log threat intelligence"""
        self.logger.info(
            f"THREAT INTELLIGENCE - Type: {threat_type}, "
            f"Confidence: {confidence:.2f}, Source: {source}, "
            f"Indicators: {indicators}"
        )

class PerformanceLogger:
    """Logger for performance metrics"""
    
    def __init__(self, logger_name: str = "performance"):
        self.logger = logging.getLogger(f"cybersecurity_simulation.{logger_name}")
    
    def log_model_performance(self, model_name: str, accuracy: float, 
                             precision: float, recall: float, f1_score: float):
        """Log ML model performance metrics"""
        self.logger.info(
            f"MODEL PERFORMANCE - {model_name}: "
            f"Accuracy={accuracy:.3f}, Precision={precision:.3f}, "
            f"Recall={recall:.3f}, F1-Score={f1_score:.3f}"
        )
    
    def log_system_performance(self, component: str, response_time: float, 
                              throughput: float, error_rate: float):
        """Log system performance metrics"""
        self.logger.info(
            f"SYSTEM PERFORMANCE - {component}: "
            f"Response Time={response_time}ms, "
            f"Throughput={throughput}/s, Error Rate={error_rate:.3f}"
        )
    
    def log_resource_usage(self, cpu_usage: float, memory_usage: float, 
                          network_usage: float):
        """Log resource usage"""
        self.logger.debug(
            f"RESOURCE USAGE - CPU: {cpu_usage:.1f}%, "
            f"Memory: {memory_usage:.1f}%, Network: {network_usage:.1f}%"
        ) 