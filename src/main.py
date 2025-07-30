#!/usr/bin/env python3
"""
Digital Twin Cybersecurity Simulation - Main Application
"""

import os
import sys
import logging
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent))

from core.simulation_engine import SimulationEngine
from core.dashboard import Dashboard
from utils.config import Config
from utils.logger import setup_logger

def main():
    """Main application entry point"""
    
    # Setup logging
    logger = setup_logger()
    logger.info("Starting Digital Twin Cybersecurity Simulation")
    
    try:
        # Load configuration
        config = Config()
        logger.info("Configuration loaded successfully")
        
        # Initialize simulation engine
        simulation = SimulationEngine(config)
        logger.info("Simulation engine initialized")
        
        # Start dashboard
        dashboard = Dashboard(simulation, config)
        logger.info("Dashboard started")
        
        # Run simulation
        simulation.run()
        
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 