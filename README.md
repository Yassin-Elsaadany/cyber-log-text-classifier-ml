# Cyber Log Text Classifier ML

A small machine-learning project that classifies security log messages into common event types such as SQL Injection, XSS, brute-force login attempts, port scans, path traversal, malware indicators, and benign activity.

This project is designed as a clean GitHub/CV project: it has a reproducible dataset, training script, saved model pipeline, prediction script, and test file.

## Features

- TF-IDF text vectorization for log messages
- Logistic Regression classifier
- Command-line prediction for new logs
- Evaluation report with accuracy and per-class metrics
- Simple, readable Python code structure
- Defensive/security-focused use case

## Project Structure

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
```

## Labels

The sample dataset includes these classes:

- `BENIGN`
- `SQL_INJECTION`
- `XSS`
- `BRUTE_FORCE`
- `PORT_SCAN`
- `PATH_TRAVERSAL`
- `MALWARE_INDICATOR`
- `AUTH_ERROR`

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt
python src/train.py
python src/predict.py "GET /login.php?id=1 union select username,password from users"
```

## Example Prediction

```bash
python src/predict.py "GET /search?q=<script>alert(1)</script>"
```

Expected style of output:

```text
Predicted label: XSS
Confidence: 0.91
```

## Evaluation

Run:

```bash
python src/evaluate.py
```

This trains the model on the sample dataset and prints a classification report.

## Important Note

This is an educational ML project, not a production IDS/SIEM. A real security system needs larger datasets, log normalization, alert enrichment, threat intelligence, tuning, and continuous validation.

## CV Description

**Cyber Log Text Classifier ML** — Built a Python machine-learning pipeline that classifies security log messages into attack categories using TF-IDF features and a Logistic Regression model. The project includes a training dataset, reproducible scripts, evaluation metrics, and CLI-based prediction for new logs.
