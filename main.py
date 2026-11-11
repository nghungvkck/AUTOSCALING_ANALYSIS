"""Train XGBoost, LightGBM, then Hybrid models for 1m, 5m, and 15m windows.

Run from the repository root with the raw log files configured in
configs/train_config.yaml available. Outputs go to forecasting/artifacts/.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from forecasting.train.train_hybrid import run as run_hybrid
from forecasting.train.train_lightgbm import run as run_lightgbm
from forecasting.train.train_xgboost import run as run_xgboost


def main(config_path: str = "configs/train_config.yaml"):
    print("=" * 60)
    print("Starting AutoScaling Forecasting Pipeline")
    print("=" * 60)

    print("\n[1/3] Training XGBoost models...")
    run_xgboost(config_path)

    print("\n[2/3] Training LightGBM models...")
    run_lightgbm(config_path)

    print("\n[3/3] Training Hybrid models...")
    run_hybrid(config_path)

    print("\n" + "=" * 60)
    print("Pipeline completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
