# Cyber Log Text Classifier ML

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Enabled-green)
![Security](https://img.shields.io/badge/Security-Log%20Analysis-red)
![Status](https://img.shields.io/badge/Status-Educational-blue)

A machine-learning project that classifies cybersecurity log messages into common event types such as SQL Injection, XSS, brute-force login attempts, port scans, path traversal, malware indicators, authentication errors, and benign activity.

This project includes a reproducible dataset, training script, saved model pipeline, prediction script, evaluation script, and test file.

---

## 🔍 Project Purpose

The goal of this project is to show how machine learning and natural language processing can be used to classify security-related log messages.

It demonstrates the basic workflow of:

- Preparing labeled security log data
- Converting log text into numerical features
- Training a classification model
- Evaluating model performance
- Predicting the category of new log entries

---

## 🔥 Features

- TF-IDF text vectorization for log messages
- Logistic Regression classifier
- Command-line prediction for new logs
- Evaluation report with accuracy and per-class metrics
- Simple and readable Python code structure
- Defensive/security-focused use case
- Test file for basic project validation

---

## 🧠 Labels

The sample dataset includes these classes:

- BENIGN
- SQL_INJECTION
- XSS
- BRUTE_FORCE
- PORT_SCAN
- PATH_TRAVERSAL
- MALWARE_INDICATOR
- AUTH_ERROR

---

## 🧰 Tech Stack

- Python
- scikit-learn
- pandas
- TF-IDF
- Logistic Regression
- NLP basics

---

## 📁 Project Structure

cyber-log-text-classifier-ml/

- data/logs.csv
- docs/cv_summary.md
- src/train.py
- src/evaluate.py
- src/predict.py
- tests/test_training.py
- requirements.txt
- README.md

---

## 🚀 Quick Start

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Activate it on Linux/macOS:

source .venv/bin/activate

Install requirements:

pip install -r requirements.txt

Train the model:

python src/train.py

Predict a new log message:

python src/predict.py "GET /login.php?id=1 union select username,password from users"

---

## 🧪 Example Prediction

Command:

python src/predict.py "GET /search?q=<script>alert(1)</script>"

Expected style of output:

Predicted label: XSS  
Confidence: 0.91

---

## 📊 Evaluation

Run:

python src/evaluate.py

This trains the model on the sample dataset and prints a classification report with accuracy and per-class metrics.

---

## ⚠️ Important Note

This is an educational machine-learning project, not a production IDS or SIEM.

A real security monitoring system would need:

- Larger and more realistic datasets
- Log normalization
- Alert enrichment
- Threat intelligence integration
- Model tuning
- Continuous validation
- False-positive and false-negative analysis

---

## 📌 CV Description

Cyber Log Text Classifier ML — Built a Python machine-learning pipeline that classifies cybersecurity log messages into attack and benign categories using TF-IDF features and a Logistic Regression model. The project includes a training dataset, reproducible scripts, evaluation metrics, and CLI-based prediction for new logs.

---

## 👨‍💻 Author

Yassin Elsaadany

GitHub: https://github.com/Yassin-Elsaadany
