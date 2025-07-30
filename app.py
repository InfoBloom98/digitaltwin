#!/usr/bin/env python3
"""
Digital Twin Cybersecurity Simulation - Streamlit App
"""

import streamlit as st
import sys
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime, timedelta
import numpy as np

# Add src to path
sys.path.append(str(Path(__file__).parent / 'src'))

# Import simulation components
try:
    from utils.config import Config
    from utils.logger import setup_logger
    from data.digital_twin_generator import DigitalTwinGenerator
    from security.vulnerability_detector import VulnerabilityDetector
    from security.attack_predictor import AttackPredictor
    from security.security_evaluator import SecurityEvaluator
    from security.resilience_enhancer import ResilienceEnhancer
    from models.anomaly_detector import AnomalyDetector
except ImportError as e:
    st.error(f"Import error: {e}")
    st.info("Please ensure all required modules are available in the src directory")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Digital Twin Cybersecurity Simulation",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .alert-high {
        background-color: #ffebee;
        border-left: 4px solid #f44336;
    }
    .alert-medium {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
    }
    .alert-low {
        background-color: #e8f5e8;
        border-left: 4px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_simulation():
    """Initialize simulation components with caching"""
    config = Config()
    logger = setup_logger()
    
    generator = DigitalTwinGenerator(config)
    detector = VulnerabilityDetector(config)
    predictor = AttackPredictor(config)
    evaluator = SecurityEvaluator(config)
    enhancer = ResilienceEnhancer(config)
    anomaly_detector = AnomalyDetector(config)
    
    return {
        'config': config,
        'logger': logger,
        'generator': generator,
        'detector': detector,
        'predictor': predictor,
        'evaluator': evaluator,
        'enhancer': enhancer,
        'anomaly_detector': anomaly_detector
    }

@st.cache_data
def generate_simulation_data(num_entities=50):
    """Generate simulation data with caching"""
    components = initialize_simulation()
    
    # Generate digital twins
    entities = components['generator'].generate_entities(num_entities)
    entities_dict = {entity['id']: entity for entity in entities}
    
    # Detect vulnerabilities
    vulnerabilities = components['detector'].detect_vulnerabilities(entities_dict)
    
    # Predict attacks
    attack_scenarios = components['predictor'].predict_attacks(entities_dict, [])
    
    # Evaluate security
    security_score = components['evaluator'].evaluate_security(entities_dict, [])
    
    # Generate recommendations
    recommendations = components['enhancer'].generate_recommendations(
        entities_dict, [], {'security_score': security_score}
    )
    
    # Detect anomalies
    components['anomaly_detector'].train(entities_dict)
    anomalies = components['anomaly_detector'].detect_anomalies(entities_dict)
    
    return {
        'entities': entities,
        'entities_dict': entities_dict,
        'vulnerabilities': vulnerabilities,
        'attack_scenarios': attack_scenarios,
        'security_score': security_score,
        'recommendations': recommendations,
        'anomalies': anomalies
    }

def main_dashboard():
    """Main dashboard page"""
    st.markdown('<h1 class="main-header">🔒 Digital Twin Cybersecurity Simulation</h1>', unsafe_allow_html=True)
    
    # Sidebar controls
    st.sidebar.header("🎛️ Simulation Controls")
    
    num_entities = st.sidebar.slider(
        "Number of Digital Twins",
        min_value=10,
        max_value=200,
        value=50,
        step=10
    )
    
    if st.sidebar.button("🔄 Refresh Simulation", type="primary"):
        st.cache_data.clear()
        st.rerun()
    
    # Load simulation data
    with st.spinner("🔄 Loading simulation data..."):
        data = generate_simulation_data(num_entities)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🏥 Digital Twins",
            value=len(data['entities']),
            delta=f"+{len(data['entities'])} entities"
        )
    
    with col2:
        st.metric(
            label="🔍 Vulnerabilities",
            value=len(data['vulnerabilities']),
            delta=f"{len(data['vulnerabilities'])} detected"
        )
    
    with col3:
        st.metric(
            label="🎯 Attack Scenarios",
            value=len(data['attack_scenarios']),
            delta=f"{len(data['attack_scenarios'])} predicted"
        )
    
    with col4:
        security_color = "normal"
        if data['security_score'] < 40:
            security_color = "inverse"
        elif data['security_score'] < 60:
            security_color = "off"
        
        st.metric(
            label="📊 Security Score",
            value=f"{data['security_score']:.1f}/100",
            delta=f"{data['security_score']:.1f} points",
            delta_color=security_color
        )
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview", "🔍 Vulnerabilities", "🎯 Attack Scenarios", 
        "🚨 Anomalies", "💡 Recommendations"
    ])
    
    with tab1:
        show_overview(data)
    
    with tab2:
        show_vulnerabilities(data)
    
    with tab3:
        show_attack_scenarios(data)
    
    with tab4:
        show_anomalies(data)
    
    with tab5:
        show_recommendations(data)

def show_overview(data):
    """Show overview dashboard"""
    st.header("📊 System Overview")
    
    # Entity distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏥 Digital Twin Distribution")
        entity_types = pd.DataFrame(data['entities'])
        entity_counts = entity_types['type'].value_counts()
        
        fig = px.pie(
            values=entity_counts.values,
            names=entity_counts.index,
            title="Entity Types Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🔍 Vulnerability Severity")
        if data['vulnerabilities']:
            vuln_df = pd.DataFrame(data['vulnerabilities'])
            severity_counts = vuln_df['severity'].value_counts()
            
            fig = px.bar(
                x=severity_counts.index,
                y=severity_counts.values,
                title="Vulnerabilities by Severity",
                color=severity_counts.values,
                color_continuous_scale="RdYlGn_r"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No vulnerabilities detected")
    
    # Security timeline
    st.subheader("📈 Security Score Timeline")
    
    # Generate mock timeline data
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), periods=30, freq='D')
    scores = [data['security_score'] + np.random.normal(0, 5) for _ in range(30)]
    scores = [max(0, min(100, score)) for score in scores]
    
    timeline_df = pd.DataFrame({
        'Date': dates,
        'Security Score': scores
    })
    
    fig = px.line(
        timeline_df,
        x='Date',
        y='Security Score',
        title="Security Score Over Time"
    )
    fig.add_hline(y=80, line_dash="dash", line_color="green", annotation_text="Excellent")
    fig.add_hline(y=60, line_dash="dash", line_color="orange", annotation_text="Good")
    fig.add_hline(y=40, line_dash="dash", line_color="red", annotation_text="Poor")
    
    st.plotly_chart(fig, use_container_width=True)

def show_vulnerabilities(data):
    """Show vulnerabilities analysis"""
    st.header("🔍 Vulnerability Analysis")
    
    if not data['vulnerabilities']:
        st.info("No vulnerabilities detected in the current simulation.")
        return
    
    vuln_df = pd.DataFrame(data['vulnerabilities'])
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_severity = st.multiselect(
            "Filter by Severity",
            options=vuln_df['severity'].unique(),
            default=vuln_df['severity'].unique()
        )
    
    with col2:
        selected_type = st.multiselect(
            "Filter by Type",
            options=vuln_df['type'].unique(),
            default=vuln_df['type'].unique()
        )
    
    with col3:
        selected_status = st.multiselect(
            "Filter by Status",
            options=vuln_df['status'].unique() if 'status' in vuln_df.columns else ['open'],
            default=vuln_df['status'].unique() if 'status' in vuln_df.columns else ['open']
        )
    
    # Filter data
    filtered_vuln = vuln_df[
        (vuln_df['severity'].isin(selected_severity)) &
        (vuln_df['type'].isin(selected_type))
    ]
    
    if 'status' in vuln_df.columns:
        filtered_vuln = filtered_vuln[vuln_df['status'].isin(selected_status)]
    
    # Vulnerability statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        high_vulns = len(filtered_vuln[filtered_vuln['severity'] == 'high'])
        st.metric("🔴 High Severity", high_vulns)
    
    with col2:
        medium_vulns = len(filtered_vuln[filtered_vuln['severity'] == 'medium'])
        st.metric("🟡 Medium Severity", medium_vulns)
    
    with col3:
        low_vulns = len(filtered_vuln[filtered_vuln['severity'] == 'low'])
        st.metric("🟢 Low Severity", low_vulns)
    
    # Vulnerability details table
    st.subheader("📋 Vulnerability Details")
    
    # Prepare table data
    display_cols = ['id', 'title', 'severity', 'type', 'description', 'cvss_score']
    available_cols = [col for col in display_cols if col in filtered_vuln.columns]
    
    if available_cols:
        st.dataframe(
            filtered_vuln[available_cols].head(20),
            use_container_width=True
        )
    else:
        st.dataframe(filtered_vuln.head(20), use_container_width=True)

def show_attack_scenarios(data):
    """Show attack scenarios analysis"""
    st.header("🎯 Attack Scenarios")
    
    if not data['attack_scenarios']:
        st.info("No attack scenarios predicted in the current simulation.")
        return
    
    scenarios_df = pd.DataFrame(data['attack_scenarios'])
    
    # Attack scenario statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_scenarios = len(scenarios_df)
        st.metric("🎯 Total Scenarios", total_scenarios)
    
    with col2:
        if 'probability' in scenarios_df.columns:
            avg_prob = scenarios_df['probability'].mean()
            st.metric("📊 Avg Probability", f"{avg_prob:.2%}")
        else:
            st.metric("📊 Scenarios", total_scenarios)
    
    with col3:
        if 'impact' in scenarios_df.columns:
            high_impact = len(scenarios_df[scenarios_df['impact'] == 'high'])
            st.metric("🔥 High Impact", high_impact)
        else:
            unique_types = scenarios_df['type'].nunique()
            st.metric("🔍 Attack Types", unique_types)
    
    # Attack scenario visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Attack Types Distribution")
        attack_counts = scenarios_df['type'].value_counts()
        
        fig = px.bar(
            x=attack_counts.index,
            y=attack_counts.values,
            title="Attack Scenarios by Type"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Attack Probability Distribution")
        if 'probability' in scenarios_df.columns:
            fig = px.histogram(
                scenarios_df,
                x='probability',
                title="Attack Probability Distribution",
                nbins=20
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Probability data not available")
    
    # Attack scenario details
    st.subheader("📋 Attack Scenario Details")
    st.dataframe(scenarios_df.head(20), use_container_width=True)

def show_anomalies(data):
    """Show anomalies analysis"""
    st.header("🚨 Anomaly Detection")
    
    if not data['anomalies']:
        st.info("No anomalies detected in the current simulation.")
        return
    
    anomalies_df = pd.DataFrame(data['anomalies'])
    
    # Anomaly statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_anomalies = len(anomalies_df)
        st.metric("🚨 Total Anomalies", total_anomalies)
    
    with col2:
        if 'anomaly_score' in anomalies_df.columns:
            avg_score = anomalies_df['anomaly_score'].mean()
            st.metric("📊 Avg Anomaly Score", f"{avg_score:.3f}")
        else:
            st.metric("📊 Anomalies", total_anomalies)
    
    with col3:
        if 'severity' in anomalies_df.columns:
            high_severity = len(anomalies_df[anomalies_df['severity'] == 'high'])
            st.metric("🔴 High Severity", high_severity)
        else:
            st.metric("🔍 Detected", total_anomalies)
    
    # Anomaly visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚨 Anomaly Severity Distribution")
        if 'severity' in anomalies_df.columns:
            severity_counts = anomalies_df['severity'].value_counts()
            
            fig = px.pie(
                values=severity_counts.values,
                names=severity_counts.index,
                title="Anomalies by Severity"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Severity data not available")
    
    with col2:
        st.subheader("📊 Anomaly Score Distribution")
        if 'anomaly_score' in anomalies_df.columns:
            fig = px.histogram(
                anomalies_df,
                x='anomaly_score',
                title="Anomaly Score Distribution",
                nbins=20
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Anomaly score data not available")
    
    # Anomaly details
    st.subheader("📋 Anomaly Details")
    st.dataframe(anomalies_df.head(20), use_container_width=True)

def show_recommendations(data):
    """Show security recommendations"""
    st.header("💡 Security Recommendations")
    
    if not data['recommendations']:
        st.info("No recommendations generated in the current simulation.")
        return
    
    recommendations_df = pd.DataFrame(data['recommendations'])
    
    # Recommendation statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_recs = len(recommendations_df)
        st.metric("💡 Total Recommendations", total_recs)
    
    with col2:
        if 'priority' in recommendations_df.columns:
            high_priority = len(recommendations_df[recommendations_df['priority'] == 'high'])
            st.metric("🔴 High Priority", high_priority)
        else:
            st.metric("📊 Recommendations", total_recs)
    
    with col3:
        if 'category' in recommendations_df.columns:
            unique_categories = recommendations_df['category'].nunique()
            st.metric("📂 Categories", unique_categories)
        else:
            st.metric("📊 Total", total_recs)
    
    # Priority filter
    if 'priority' in recommendations_df.columns:
        priority_filter = st.selectbox(
            "Filter by Priority",
            options=['All'] + list(recommendations_df['priority'].unique())
        )
        
        if priority_filter != 'All':
            recommendations_df = recommendations_df[recommendations_df['priority'] == priority_filter]
    
    # Display recommendations
    st.subheader("📋 Security Recommendations")
    
    for idx, rec in recommendations_df.iterrows():
        priority_color = {
            'high': 'alert-high',
            'medium': 'alert-medium',
            'low': 'alert-low'
        }.get(rec.get('priority', 'medium'), 'alert-medium')
        
        st.markdown(f"""
        <div class="metric-card {priority_color}">
            <h4>{rec.get('title', f'Recommendation {idx+1}')}</h4>
            <p><strong>Priority:</strong> {rec.get('priority', 'medium').title()}</p>
            <p><strong>Description:</strong> {rec.get('description', 'No description available')}</p>
            {f'<p><strong>Category:</strong> {rec.get("category", "General")}</p>' if 'category' in rec else ''}
            {f'<p><strong>Impact:</strong> {rec.get("impact", "Medium")}</p>' if 'impact' in rec else ''}
        </div>
        """, unsafe_allow_html=True)
        st.write("")

def real_time_monitoring():
    """Real-time monitoring page"""
    st.header("🔄 Real-Time Monitoring")
    
    st.info("This page would show real-time monitoring of digital twin security status.")
    
    # Placeholder for real-time data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🟢 Online", 45, delta=2)
    
    with col2:
        st.metric("🔴 Offline", 3, delta=-1)
    
    with col3:
        st.metric("⚠️ Warning", 2, delta=0)
    
    with col4:
        st.metric("🚨 Alert", 1, delta=1)
    
    # Real-time chart placeholder
    st.subheader("📈 Real-Time Security Metrics")
    
    # Generate mock real-time data
    timestamps = pd.date_range(start=datetime.now() - timedelta(hours=1), periods=60, freq='min')
    security_scores = [75 + np.random.normal(0, 3) for _ in range(60)]
    security_scores = [max(0, min(100, score)) for score in security_scores]
    
    real_time_df = pd.DataFrame({
        'Timestamp': timestamps,
        'Security Score': security_scores
    })
    
    fig = px.line(
        real_time_df,
        x='Timestamp',
        y='Security Score',
        title="Real-Time Security Score"
    )
    st.plotly_chart(fig, use_container_width=True)

def settings_page():
    """Settings and configuration page"""
    st.header("⚙️ Settings & Configuration")
    
    st.subheader("🔧 Simulation Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.number_input("Default Number of Entities", min_value=10, max_value=500, value=50)
        st.selectbox("Log Level", ["INFO", "DEBUG", "WARNING", "ERROR"])
        st.checkbox("Enable Real-time Monitoring", value=True)
    
    with col2:
        st.number_input("Security Score Threshold", min_value=0, max_value=100, value=60)
        st.selectbox("Alert Level", ["Low", "Medium", "High", "Critical"])
        st.checkbox("Auto-refresh Dashboard", value=True)
    
    st.subheader("📊 Display Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.selectbox("Chart Theme", ["plotly", "plotly_white", "plotly_dark"])
        st.number_input("Refresh Interval (seconds)", min_value=5, max_value=300, value=30)
    
    with col2:
        st.selectbox("Data Export Format", ["CSV", "JSON", "Excel"])
        st.checkbox("Show Debug Information", value=False)

def main():
    """Main application function"""
    # Navigation
    st.sidebar.title("🔒 Navigation")
    
    page = st.sidebar.selectbox(
        "Choose a page",
        ["📊 Dashboard", "🔄 Real-Time Monitoring", "⚙️ Settings"]
    )
    
    if page == "📊 Dashboard":
        main_dashboard()
    elif page == "🔄 Real-Time Monitoring":
        real_time_monitoring()
    elif page == "⚙️ Settings":
        settings_page()

if __name__ == "__main__":
    main() 