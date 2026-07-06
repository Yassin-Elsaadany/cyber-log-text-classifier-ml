from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "logs.csv"
MODEL_DIR = ROOT_DIR / "models"
MODEL_PATH = MODEL_DIR / "log_classifier.joblib"


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and validate the log dataset."""
    data = pd.read_csv(path)
    required_columns = {"message", "label"}
    missing = required_columns.difference(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")
    data = data.dropna(subset=["message", "label"])
    return data


def build_pipeline() -> Pipeline:
    """Create the ML pipeline used for training and prediction."""
    return Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1, 2),
                    min_df=1,
                    max_features=5000,
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=42,
                ),
            ),
        ]
    )


def train_model(save_model: bool = True) -> Pipeline:
    """Train the model and optionally save it to disk."""
    data = load_dataset()
    x_train, x_test, y_train, y_test = train_test_split(
        data["message"],
        data["label"],
        test_size=0.25,
        random_state=42,
        stratify=data["label"],
    )

    pipeline = build_pipeline()
    pipeline.fit(x_train, y_train)

    predictions = pipeline.predict(x_test)
    print("\nEvaluation on hold-out test set:\n")
    print(classification_report(y_test, predictions, zero_division=0))

    if save_model:
        MODEL_DIR.mkdir(exist_ok=True)
        joblib.dump(pipeline, MODEL_PATH)
        print(f"\nModel saved to: {MODEL_PATH}")

    return pipeline


if __name__ == "__main__":
    train_model(save_model=True)
