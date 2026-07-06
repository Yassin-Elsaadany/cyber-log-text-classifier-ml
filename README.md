# Cyber Log Text Classifier ML

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Enabled-green)
![Security](https://img.shields.io/badge/Security-Log%20Analysis-red)
![Status](https://img.shields.io/badge/Status-Educational-blue)

A machine-learning project that classifies cybersecurity log messages into common event types such as SQL Injection, XSS, brute-force login attempts, port scans, path traversal, malware indicators, authentication errors, and benign activity.

This project is designed as a clean GitHub/CV project. It includes a reproducible dataset, training script, saved model pipeline, prediction script, evaluation script, and test file.

---

## 🔍 Project Purpose

The goal of this project is to show how machine learning and natural language processing can be used to classify security-related log messages.

It is not a replacement for a real IDS or SIEM, but it demonstrates the basic workflow of:

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

- `BENIGN`
- `SQL_INJECTION`
- `XSS`
- `BRUTE_FORCE`
- `PORT_SCAN`
- `PATH_TRAVERSAL`
- `MALWARE_INDICATOR`
- `AUTH_ERROR`

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

```text
cyber-log-text-classifier-ml/
├── data/
│   └── logs.csv
├── docs/
│   └── cv_summary.md
├── src/
│   ├── __init__.py
│   ├── evaluate.py
│   ├── predict.py
│   └── train.py
├── tests/
│   └── test_training.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
