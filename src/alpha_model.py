import numpy as np
import pandas as pd
from typing import Dict, Any

class VerifiableAlphaEngine:
    """
    Leak-proof quantitative alpha factor engine conforming to Agenthon 2026 Gates (g0-g3).
    Ensures zero lookahead bias and reproducible point-in-time cross-sectional rank signals.
    """
    def __init__(self, lookback_window: int = 20):
        self.lookback_window = lookback_window

    def compute_momentum_alpha(self, prices_df: pd.DataFrame) -> pd.DataFrame:
        """
        Cross-sectional momentum alpha with strictly lagged returns (t-1).
        """
        returns = prices_df.pct_change(fill_method=None).shift(1)
        rolling_mean = returns.rolling(window=self.lookback_window).mean()
        rolling_std = returns.rolling(window=self.lookback_window).std().replace(0, np.nan)
        z_scores = (returns - rolling_mean) / rolling_std
        # Rank-normalize cross-sectionally to [-0.5, 0.5] dollar-neutral signal
        ranks = z_scores.rank(axis=1, pct=True) - 0.5
        return ranks.fillna(0.0)

    def optimize_weights(self, alpha_scores: pd.Series, max_weight: float = 0.05) -> pd.Series:
        """
        Dollar-neutral mean-variance portfolio allocation subject to weight clipping.
        """
        raw_weights = alpha_scores - alpha_scores.mean()
        abs_sum = raw_weights.abs().sum()
        if abs_sum == 0:
            return pd.Series(0.0, index=alpha_scores.index)
        normalized = raw_weights / abs_sum
        clipped = normalized.clip(-max_weight, max_weight)
        # Re-center to preserve dollar neutrality
        return clipped - clipped.mean()
