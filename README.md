# 🔒 Digital Twin Cybersecurity Simulation

## 🎓 **Educational Overview**

Welcome to the **Digital Twin Cybersecurity Simulation** - an interactive learning platform designed to help students understand and practice cybersecurity concepts in the context of healthcare digital twins. This simulation provides hands-on experience with real-world cybersecurity challenges faced by modern healthcare systems.

### **What is a Digital Twin?**
A **Digital Twin** is a virtual representation of a physical system, process, or service. In healthcare, digital twins can represent:
- 🏥 Medical devices (MRI machines, ventilators, patient monitors)
- 💊 Pharmaceutical manufacturing processes
- 🏨 Hospital infrastructure and networks
- 👥 Patient data and treatment protocols

### **Why Cybersecurity Matters in Healthcare Digital Twins?**
Healthcare digital twins contain sensitive patient data and control critical medical equipment. Cyberattacks on these systems can:
- **Compromise patient privacy** and medical records
- **Disrupt life-saving medical devices**
- **Cause system failures** during critical procedures
- **Lead to regulatory violations** and legal consequences

## 🎯 **Learning Objectives**

This simulation will help you understand:

1. **🔍 Vulnerability Detection**: How to identify security weaknesses in digital twin systems
2. **🎯 Attack Prediction**: How to anticipate and model potential cyber threats
3. **📊 Security Evaluation**: How to assess the effectiveness of security measures
4. **🛡️ Resilience Enhancement**: How to build robust cybersecurity defenses
5. **📈 Real-time Monitoring**: How to continuously monitor system security
6. **🚨 Incident Response**: How to respond to security incidents effectively

## 🎯 **Technical Objectives**

1. **🔍 Detect Vulnerabilities:** Identify vulnerabilities in digital twins using ML-based analysis
2. **🎯 Predict Attack Scenarios:** Predict potential cyberattack scenarios and their likelihood
3. **📊 Evaluate Security Measures:** Assess effectiveness of existing security measures
4. **🛡️ Enhance Cybersecurity Resilience:** Develop a robust cybersecurity framework

## 🏗️ **Project Structure**

```
├── app.py                   # 🖥️ Main Streamlit application (Interactive Dashboard)
├── demo.py                  # 💻 Command-line demo script
├── run_app.py              # 🚀 Python launcher script
├── run_app.bat             # 🪟 Windows batch launcher
├── src/
│   ├── core/               # 🔧 Core simulation components
│   ├── models/             # 🤖 ML models for different tasks
│   ├── data/               # 📊 Data processing and generation
│   ├── security/           # 🛡️ Security assessment modules
│   ├── visualization/      # 📈 Dashboard and visualization
│   └── utils/              # 🛠️ Utility functions
├── data/                   # 📁 Sample data and datasets
├── config/                 # ⚙️ Configuration files
├── tests/                  # 🧪 Unit tests
├── docs/                   # 📚 Documentation
└── notebooks/              # 📓 Jupyter notebooks for analysis
```

### **Key Files Explained:**
- **`app.py`**: The main interactive dashboard where you'll spend most of your time
- **`demo.py`**: A command-line version to understand the simulation logic
- **`run_app.py`** & **`run_app.bat`**: Easy launchers to start the application
- **`src/`**: Contains all the simulation logic and algorithms

## 🚀 **Quick Start Guide**

### **Prerequisites**
- **Python 3.8 or higher** (3.9+ recommended)
- **pip package manager** (usually comes with Python)
- **Web browser** (Chrome, Firefox, Safari, or Edge)

### **What You'll Need to Know:**
- Basic understanding of cybersecurity concepts
- Familiarity with Python (helpful but not required)
- Interest in healthcare technology and digital twins

### **Installation Options**

#### **Option 1: Full Installation (Recommended for Students)**
```bash
# Install all dependencies including ML libraries
pip install -r requirements.txt
```
*This gives you access to all features and machine learning capabilities.*

#### **Option 2: Minimal Installation (If you encounter dependency issues)**
```bash
# Install core dependencies only
pip install -r requirements-minimal.txt
```
*Use this if you have limited system resources or encounter installation problems.*

#### **Option 3: Virtual Environment (Recommended for isolation)**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
*This keeps the simulation separate from other Python projects on your computer.*

### **Troubleshooting Common Issues**

#### **Python Version Issues**
If you encounter Python version compatibility errors:
1. Use Python 3.8-3.11 (3.9+ recommended)
2. Try the minimal requirements: `pip install -r requirements-minimal.txt`
3. Update pip: `python -m pip install --upgrade pip`

#### **Package Installation Issues**
If specific packages fail to install:
1. Install system dependencies first (on Linux):
   ```bash
   sudo apt-get update
   sudo apt-get install python3-dev build-essential
   ```
2. Try installing packages individually:
   ```bash
   pip install numpy pandas scikit-learn streamlit
   ```

#### **ML Library Issues**
If TensorFlow/PyTorch installation fails:
1. Use the minimal requirements file
2. Install CPU-only versions:
   ```bash
   pip install tensorflow-cpu
   # or
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   ```

#### **Streamlit Issues**
If the dashboard doesn't load:
1. Make sure Streamlit is installed: `pip install streamlit`
2. Check if port 8501 is available
3. Try a different port: `streamlit run app.py --server.port 8502`

### Running the System

1. **Run the Demo:**
   ```bash
   python demo.py
   ```

2. **Run the Streamlit App:**
   
   **Option A: Direct Streamlit command**
   ```bash
   streamlit run app.py
   ```
   
   **Option B: Using the launcher script**
   ```bash
   python run_app.py
   ```
   
   **Option C: With custom configuration**
   ```bash
   streamlit run app.py --server.port 8501 --server.address localhost
   ```
   
   **Option D: Windows users (double-click)**
   ```bash
   run_app.bat
   ```

3. **Access the Dashboard:**
   - The Streamlit app will automatically open in your default browser
   - If it doesn't open automatically, navigate to: **http://localhost:8501**
   - The app runs on port 8501 by default

4. **Run Tests:**
   ```bash
   python -m pytest tests/
   ```

## 🔧 Features

### Vulnerability Detection
- Network traffic analysis
- Anomaly detection in system behavior
- Configuration vulnerability scanning
- Zero-day threat identification

### Attack Prediction
- ML-based attack scenario modeling
- Threat intelligence integration
- Risk assessment and scoring
- Attack path prediction

### Security Evaluation
- Penetration testing simulation
- Security control effectiveness analysis
- Compliance assessment
- Incident response evaluation

### Resilience Enhancement
- Automated security recommendations
- Adaptive security policies
- Real-time threat response
- Continuous monitoring and learning

## 📊 Streamlit Dashboard Features

### 🎛️ **Interactive Dashboard**
- Multi-page navigation with real-time updates
- Sidebar controls for simulation parameters
- Responsive design that works on desktop and mobile

### 📈 **Security Metrics & Visualizations**
- Live security score tracking with color-coded indicators
- Interactive Plotly charts for entity distribution and vulnerability analysis
- Real-time security timeline with trend analysis
- Attack scenario probability distributions

### 🔍 **Advanced Filtering & Analysis**
- Filter vulnerabilities by severity, type, and status
- Search and filter attack scenarios by probability and impact
- Anomaly detection with severity-based filtering
- Priority-based recommendation filtering

### 🚨 **Real-time Monitoring**
- Live security metrics dashboard
- Real-time anomaly detection alerts
- System status monitoring (online/offline/warning/alert)
- Continuous security score tracking

### ⚙️ **Configuration & Settings**
- Customizable simulation parameters
- Display settings and chart themes
- Export capabilities for data analysis
- Debug information and logging controls

## 🔒 Security Considerations

- All sensitive data is encrypted
- Secure communication protocols
- Access control and authentication
- Audit logging and monitoring

## 📈 Performance Metrics

- Detection accuracy: >95%
- False positive rate: <2%
- Response time: <100ms
- System availability: 99.9%

## 🤝 Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 