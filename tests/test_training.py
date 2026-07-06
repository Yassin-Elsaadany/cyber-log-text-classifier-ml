from pathlib import Path

import pandas as pd


def test_dataset_has_required_columns():
    data_path = Path(__file__).resolve().parents[1] / "data" / "logs.csv"
    data = pd.read_csv(data_path)
    assert {"message", "label"}.issubset(data.columns)
    assert len(data) >= 40


def test_each_label_has_multiple_examples():
    data_path = Path(__file__).resolve().parents[1] / "data" / "logs.csv"
    data = pd.read_csv(data_path)
    counts = data["label"].value_counts()
    assert counts.min() >= 5
