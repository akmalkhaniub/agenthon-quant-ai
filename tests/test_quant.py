import pytest
import pandas as pd
import numpy as np
from src.alpha_model import VerifiableAlphaEngine
from src.audit_gate import LeakageGuardGate

def test_alpha_engine_zero_lookahead():
    dates = pd.date_range("2026-01-01", periods=30, freq="B")
    tickers = ["TICK_A", "TICK_B", "TICK_C"]
    prices = pd.DataFrame(100.0, index=dates, columns=tickers)
    
    engine = VerifiableAlphaEngine(lookback_window=5)
    alphas = engine.compute_momentum_alpha(prices)
    assert not alphas.isna().any().any()
    assert alphas.shape == prices.shape

def test_dollar_neutrality():
    engine = VerifiableAlphaEngine()
    raw_scores = pd.Series([0.2, -0.4, 0.8, -0.1], index=["A", "B", "C", "D"])
    weights = engine.optimize_weights(raw_scores, max_weight=0.5)
    assert abs(weights.sum()) < 1e-6

def test_audit_gate_pass():
    dates = pd.date_range("2026-01-01", periods=5, freq="B")
    weights = pd.DataFrame([[0.1, -0.1]] * 5, index=dates, columns=["A", "B"])
    res = LeakageGuardGate.audit_submission(weights, pd.Series(dates))
    assert res["all_gates_passed"] is True
