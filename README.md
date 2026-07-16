# SentinelAI-FinSpark2026
AI-powered Insider Threat Detection and Quantum-Secure Access Control for Banking Systems.
# AI Driven Insider Threat Detection System

## Problem
Detect privileged access misuse and insider threats by analyzing cybersecurity telemetry.

## Solution
This prototype uses machine learning anomaly detection to identify unusual user behaviour such as:

- Excessive file access
- Multiple failed login attempts
- Unauthorized privilege changes

## Technology Used

- Python
- Machine Learning
- Isolation Forest Algorithm
- Cybersecurity Log Analysis

## Workflow

User Activity Logs → Feature Extraction → AI Anomaly Detection → Risk Identification


## System Architecture

User Activity Logs
        |
        ↓
Data Preprocessing
        |
        ↓
AI Anomaly Detection Model
(Isolation Forest)
        |
        ↓
Risk Scoring Engine
        |
        ↓
Threat Alert Generation


## Key Features

- Detects abnormal privileged account behaviour
- Identifies suspicious login patterns
- Monitors excessive file access activity
- Assigns risk levels to users
- Supports banking cybersecurity scenarios


## Machine Learning Approach

The prototype uses Isolation Forest, an unsupervised machine learning algorithm, to identify anomalous behaviour without requiring labelled attack data.


## Future Enhancements

- Real-time SIEM integration
- User Behaviour Analytics (UBA)
- Automated incident response
- Blockchain-based audit trails
- Quantum-resistant authentication
