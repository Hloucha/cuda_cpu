---
applyTo: "**"
---

# Copilot Instructions

## Answers
- Start every new chat with "Instructions used".
- Start every new chat with a joke on data science.
- Keep answers short. Code first, then explain briefly only if needed.
- Say clearly when you are unsure. Do not make up APIs or parameters.
- Answer in the language of the question (English or German).

## Context
- Data scientist: small datasets, data reshaping, DoE, modeling, optimization, statistical tests.
- VS Code, interactive `# %%` cells (ipykernel), Python 3.11+.
- Packages: managed with **uv** (`uv add <pkg>`, `uv run`). Never use `pip install`. Dependencies are listed in `pyproject.toml`.
- Repos are mostly on GitLab. Never put credentials, internal paths, or confidential data in code.

## Code Style
- Write concise, readable code. No boilerplate and no over-engineering.
- Comment only non-obvious logic. Add short docstrings (NumPy style) for reusable functions.
- Use PEP 8, snake_case, type hints for functions.
- Organize scripts into `# %% Section` cells. Imports go at the top.
- Don't rely on `__file__` in `# %%` cells; it isn't defined in interactive mode.
- Ask before adding a new dependency.

## Data
- Use pandas DataFrames. Prefer tidy/long format (`melt`, `pivot_table`) and method chaining.
- Use `.copy()` for derived DataFrames. Never overwrite raw data files.
- Handle missing values explicitly and never drop them silently.
- Read and write CSV/Excel with explicit parameters (`sep`, `decimal`, `encoding`).

## Statistics & Modeling
- **statsmodels**: Use the formula API (`smf.ols`, `smf.mixedlm`) for inference, ANOVA, mixed models, and DoE/RSM models.
- **scikit-learn**: Use `Pipeline` for prediction. Use cross-validation. Set `random_state` to 42.
- **scipy**: Use `scipy.stats` for tests and `scipy.optimize` for optimization.
- Name the test and its assumptions, and check them (residuals, normality, variance).
- Report effect sizes and confidence intervals, not only p-values. Correct for multiple comparisons when needed.
- Prefer simple, interpretable models for small datasets.

## Plots
- Use matplotlib and seaborn. Label axes with units and use colorblind-friendly palettes.
- Show plots interactively. Use `plt.close()` only in batch scripts.
