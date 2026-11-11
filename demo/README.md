# DataFlow Autoscaling Demo

Interactive dashboard for traffic forecasting and autoscaling decisions using machine learning models.

## Current demo behavior

The Forecast tab displays prediction CSVs from `forecasting/artifacts/predictions/`.
The Optimization tab replays those predictions with historical request counts and
compares Hybrid, Reactive, and Fixed server policies. Both tabs process files
directly in Streamlit; the API Demo tab calls the separately running FastAPI server.

`POST /forecast/metrics` runs LightGBM inference for the `5m` timeframe using
`forecasting/artifacts/models/`. The `/recommend-scaling` endpoint uses a separate
rule set from the Optimization tab, so their recommendations may differ.
Some older helpers still default to `forecasting/models/`; the Models section
below describes that older layout rather than the current training output path.

See [demo workflows and policy details](../readme_demo_policies.md) for exact
thresholds, cooldown behavior, cost assumptions, and known implementation limits.

## Features

- **Traffic Overview**: Visualize request patterns, burst detection, and events
- **Forecast Models**: LSTM (Hybrid), XGBoost, and LightGBM predictions
- **Autoscaling Decisions**: Real-time scaling recommendations based on predictions
- **Cost Analysis**: Compare reactive vs predictive scaling costs
- **REST API**: HTTP endpoints for programmatic access to predictions

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Streamlit Dashboard

```bash
streamlit run app/dashboard.py
```

### REST API Server

```bash
python api.py
```

Access API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
demo/
├── app/
│   ├── dashboard.py           # Main Streamlit app (Overview, Forecast, Autoscaling, Cost, API tabs)
│   ├── forecast_tab_simple.py # Simple single-model forecast view
│   ├── forecast_tab_plotly.py # Advanced Plotly multi-model visualization
│   └── api_demo_tab.py        # REST API demo and testing interface
├── utils/
│   ├── forecast.py            # Model forecasting & discovery (loads from ../forecasting/models)
│   ├── scaling.py             # Autoscaling decision logic (load thresholds)
│   ├── metrics_forecast.py    # Metrics calculation and display
│   └── load_data.py           # Data loading (from ../data/ - test CSVs)
├── api.py                     # FastAPI inference server (port 8000)
├── requirements.txt           # Demo-specific dependencies
└── README.md
```

## Data Source

Demo loads test data from `../data/`:

- `test_1m_autoscaling.csv` - 1-minute window traffic data
- `test_5m_autoscaling.csv` - 5-minute window traffic data
- `test_15m_autoscaling.csv` - 15-minute window traffic data

Expected columns: `timestamp`, `requests_count` (and optional `is_burst`, `is_event`, seasonal features)

## Models

Models are loaded from `../forecasting/models/` (not demo/models):

- **LSTM (Hybrid)**: Prophet baseline + LSTM residuals (`.h5`)
- **XGBoost**: Gradient boosting model (`.pkl` or `.json`)
- **LightGBM**: Light gradient boosting model (`.pkl`)

Each model is trained for 3 time windows: 1m, 5m, 15m

## Key Metrics

- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Squared Error
- **sMAPE**: Symmetric Mean Absolute Percentage Error
- **Cost Savings**: Predictive vs reactive scaling comparison
