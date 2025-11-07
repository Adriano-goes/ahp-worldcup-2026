import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- Paths ---
EXCEL_PATH = Path(r"C:\Users\31651\OneDrive\Desktop\MBA\PROJECTS\WORLD CUP 26\files\AHP_WorldCup2026_Favorites.xlsx")
OUT_CSV = EXCEL_PATH.with_name("ahp_worldcup2026_results.csv")
OUT_PNG = EXCEL_PATH.with_name("ahp_worldcup2026_barh.png")

# --- Columns expected in the Results sheet ---
TEAM_COL = "Team"
SCORE_COL = "Score (%)"

# --- Load results from Excel ---
df = pd.read_excel(EXCEL_PATH, sheet_name="Results")

# --- Sort by score (descending) and export CSV ---
df_sorted = df.sort_values(by=SCORE_COL, ascending=False).reset_index(drop=True)
df_sorted.to_csv(OUT_CSV, index=False)

# --- Plot: horizontal bars with in-bar percentage labels ---
fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.barh(df_sorted[TEAM_COL], df_sorted[SCORE_COL])

ax.set_xlabel("Score (%)")
ax.set_title("AHP — World Cup 2026 Favorites (Score %)")
ax.invert_yaxis()  # highest score on top
ax.grid(axis="x", alpha=0.2)

# Write percentage labels centered inside the bars
values = df_sorted[SCORE_COL].to_numpy()
for rect, v in zip(bars, values):
    ax.text(
        rect.get_x() + rect.get_width() / 2,
        rect.get_y() + rect.get_height() / 2,
        f"{v:.2f}%",
        ha="center", va="center",
        color="white", fontsize=10
    )

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=200)
plt.show()
plt.close()

print(f"Saved: {OUT_CSV}")
print(f"Saved: {OUT_PNG}")
