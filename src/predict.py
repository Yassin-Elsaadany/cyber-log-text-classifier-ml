from __future__ import annotations

import sys
from pathlib import Path

import joblib

ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT_DIR / "models" / "log_classifier.joblib"


def predict_log(message: str) -> tuple[str, float]:
    """Predict the class and confidence for a single log message."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model file not found. Run `python src/train.py` before prediction."
        )

    model = joblib.load(MODEL_PATH)
    label = model.predict([message])[0]

    confidence = 0.0
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([message])[0]
        confidence = float(max(probabilities))

    return label, confidence


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python src/predict.py "<log message>"')
        sys.exit(1)

    message = " ".join(sys.argv[1:])
    label, confidence = predict_log(message)
    print(f"Predicted label: {label}")
    print(f"Confidence: {confidence:.2f}")


if __name__ == "__main__":
    main()
