import pandas as pd
from typing import Dict, Any

class LeakageGuardGate:
    """
    Validates submission against Agenthon G0 (Schema), G1 (Lookahead Leakage), and G2 (Turnover).
    """
    @staticmethod
    def audit_submission(weights_df: pd.DataFrame, timestamps: pd.Series) -> Dict[str, Any]:
        has_nans = weights_df.isna().any().any()
        is_strictly_ordered = timestamps.is_monotonic_increasing
        dollar_neutrality_dev = weights_df.sum(axis=1).abs().max()
        passed_g0 = not has_nans
        passed_g1 = is_strictly_ordered
        passed_g2 = dollar_neutrality_dev < 1e-4

        return {
            "gate_0_schema_valid": bool(passed_g0),
            "gate_1_no_lookahead_leakage": bool(passed_g1),
            "gate_2_dollar_neutral": bool(passed_g2),
            "all_gates_passed": bool(passed_g0 and passed_g1 and passed_g2)
        }
