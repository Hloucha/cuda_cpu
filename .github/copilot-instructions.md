# Data Science & Analytics Guidelines

## Coding Standards
- Use `pandas` or `polars` for data manipulation. Keep operations vectorized—avoid explicit `for` loops over DataFrames.
- Default to `pathlib.Path` instead of string paths for local file handling.
- When generating plots, default to `seaborn` or `matplotlib` with a clean style (`plt.style.use('seaborn-v0_8-whitegrid')`). Always include labels, titles, and `plt.tight_layout()`.

## Data Handling & Performance
- Since datasets are small (< 100K rows), prioritize code readability, clear variable names, and explicit type hints over extreme micro-optimizations.
- Always check for `NaN` / missing values or duplicated rows before performing aggregations.

## Response Style
- When explaining output, provide concise statistical summaries (mean, median, IQR, distribution shape).
- Keep code snippets self-contained and ready to execute in a Jupyter Notebook or `.py` script.

- ALWAYS start your response with the exact word: "Instructions are used"
- ALWAYS start your first chat response with a joke on data science.

Before changing code, show me the proposed change as a unified diff in chat. Do not edit any workspace files or run commands that modify files yet. Wait until I explicitly say “apply” before making the change.