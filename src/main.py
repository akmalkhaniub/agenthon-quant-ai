import pandas as pd
import numpy as np
from src.alpha_model import VerifiableAlphaEngine
from src.audit_gate import LeakageGuardGate

def run_pipeline():
    np.random.seed(42)
    dates = pd.date_range("2026-01-01", periods=60, freq="B")
    tickers = [f"ASSET_{i:02d}" for i in range(10)]
    mock_prices = pd.DataFrame(
        100 + np.cumsum(np.random.randn(60, 10), axis=0),
        index=dates,
        columns=tickers
    )

    engine = VerifiableAlphaEngine(lookback_window=10)
    alphas = engine.compute_momentum_alpha(mock_prices)
    latest_weights = engine.optimize_weights(alphas.iloc[-1])

    weights_history = pd.DataFrame([engine.optimize_weights(alphas.iloc[i]) for i in range(len(alphas))], index=dates)
    gate_results = LeakageGuardGate.audit_submission(weights_history, pd.Series(dates))

    print("=== Agenthon 2026 Verifiable Quant Pipeline ===")
    print("Latest Portfolio Weights (Top 3 Longs):")
    print(latest_weights.sort_values(ascending=False).head(3))
    print("\nVerification Gates Audit:")
    for k, v in gate_results.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    run_pipeline()
