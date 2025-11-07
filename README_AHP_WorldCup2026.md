# AHP – FIFA World Cup 2026 Favorites

**Goal:** Identify the most likely favorites to win the FIFA World Cup 2026 using the Analytic Hierarchy Process (AHP).

## Hierarchy
- **Goal** → **5 Criteria** → **9 Teams (alternatives)**
- Criteria: Current Strength, Current Recent Form, Tactical & Coach Exp., Squad Depth & Market Value, World Cup History

## Method
1. Pairwise comparison (Saaty 1–9) of the criteria.
2. Normalize the pairwise matrix by column sums.
3. Priority weights = average of each normalized row.
4. Consistency: λ_max from (A·w)/w; CI = (λ_max − n)/(n − 1); CR = CI/RI (RI=1.12 for n=5).
5. Decision matrix: normalize each criterion column by its sum.
6. Final score per team: `=SUMPRODUCT(NormalizedRow, Weights)` → percent and rank.

## Excel structure
- **README** – overview.
- **Dataset** – raw inputs. Named ranges: `Teams`, `Criteria`, `RawDM`.
- **Pairwise** – judgments, normalized matrix, `Weights`, and consistency check.
- **Decision** – normalized decision matrix and per-team `Score` / `Score (%)`.
- **Leaderboard** – sorted ranking and chart.

Everything is in **English** and team names use uppercase (e.g., **ARGENTINA**).
Change any input (dataset or pairwise judgments) to recalculate the entire model.
