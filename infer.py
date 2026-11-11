"""
Example inference script using trained models.

This helper uses ModelPredictor, independently of the demo's CSV visualization
and metrics API. Its preprocessing and model-loading contracts need alignment
with training before treating it as a validated inference entry point.
"""

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from forecasting.inference import ModelPredictor


def predict_on_csv(
    csv_path: str,
    model_name: str = "lightgbm",
    window: str = "1m",
    artifacts_dir: str = "forecasting/artifacts",
) -> pd.DataFrame:
    """
    Load CSV, preprocess, and predict using trained model.
    
    Parameters
    ----------
    csv_path : str
        Path to CSV file with raw data
    model_name : str
        Model to use: lightgbm, xgboost, hybrid
    window : str
        Time window: 1m, 5m, 15m
    artifacts_dir : str
        Directory containing trained models
        
    Returns
    -------
    pd.DataFrame
        Predictions with timestamp, y_true, y_pred
    """
    predictor = ModelPredictor(artifacts_dir)
    data = pd.read_csv(csv_path)
    
    result = predictor.predict_batch(
        model_name=model_name,
        window=window,
        data=data,
    )
    return result


if __name__ == "__main__":
    result = predict_on_csv(
        "data/test_1m_autoscaling.csv",
        model_name="lightgbm",
        window="1m",
    )
    print(result.head(10))
    result.to_csv("inference_output.csv", index=False)
