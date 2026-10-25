# 📈 VeriQuant AI — Agenthon 2026 (NeurIPS / SQA / CEWIT)

[![Python: 3.11](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)
[![Competition: NeurIPS 2026 Track](https://img.shields.io/badge/NeurIPS%202026-Agenthon%20Track-darkred.svg)](https://agenthon.net)
[![Gates: G0-G3 Certified](https://img.shields.io/badge/Evaluation%20Gates-G0--G3%20Passing-emerald.svg)](#evaluation-gates)
[![Tests: Passing](https://img.shields.io/badge/Tests-3%2F3%20Passed-green.svg)](./tests)

> **Submission for the [NeurIPS 2026 Agenthon](https://agenthon.net)**  
> Organized by the **Society of Quantitative Analysts (SQA)** & **CEWIT (Stony Brook University)**.

VeriQuant AI is an autonomous, leak-proof quantitative alpha generation and portfolio optimization agent designed to survive automated leakage-controlled, cheat-resistant evaluation gates.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    DataIngest["📊 Point-in-Time Price Data"] --> LagEngine["⏳ Strictly Lagged Alpha Generator (t-1)"]
    LagEngine --> CrossSectional["📈 Cross-Sectional Rank Normalizer"]
    CrossSectional --> Opt["⚖️ Dollar-Neutral Mean-Variance Allocator"]
    Opt --> GateAudit["🛡️ Gate Audit Guard (G0 Schema, G1 Leakage, G2 Turnover)"]
    GateAudit --> Container["🐳 Self-Contained Docker Submission"]
```

---

## 🚀 Quickstart & Verification

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run test suite
pytest -q

# 3. Execute demo pipeline
python -m src.main
```
