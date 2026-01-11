from pathlib import Path
from typing import Optional, Union

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Keep plotting simple and compatible with minimal environments.
try:
    matplotlib.use("Agg")
except Exception:
    pass


def _ensure_out_path(out_path: Optional[Union[str, Path]], default_name: str) -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    out = Path(out_path) if out_path is not None else repo_root / "outputs" / "charts" / default_name
    out.parent.mkdir(parents=True, exist_ok=True)
    return out


def plot_attendance_vs_marks(df, out_path: Optional[Union[str, Path]] = None) -> Path:
    """Simple scatter: attendance vs average marks.

    Lightweight: no regression, no annotations, single PNG output.
    """
    out = _ensure_out_path(out_path, "attendance_vs_marks.png")

    if "attendance" not in df.columns or "average_marks" not in df.columns:
        return out

    x = df["attendance"].astype(float)
    y = df["average_marks"].astype(float)

    fig, ax = plt.subplots(figsize=(8, 5))
    sc = ax.scatter(x, y, c="#4c72b0", s=60, edgecolor="k", linewidth=0.5)

    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Average Marks")
    ax.set_title("Attendance vs Average Marks")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.xaxis.set_major_locator(mtick.MultipleLocator(10))
    ax.yaxis.set_major_locator(mtick.MultipleLocator(10))
    ax.grid(True, alpha=0.4)

    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def plot_performance_status(df, out_path: Optional[Union[str, Path]] = None) -> Path:
    """Simple bar chart of performance status.

    Lightweight: sorted bars and count annotations, single PNG output.
    """
    out = _ensure_out_path(out_path, "performance_status.png")

    cols = {c.lower(): c for c in df.columns}
    col_name = None
    for cand in ("performance_status", "performance-status", "status", "performance", "performance status"):
        if cand in cols:
            col_name = cols[cand]
            break
    if col_name is None:
        return out

    counts = df[col_name].value_counts()

    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(counts.index.astype(str), counts.values, color="#4c72b0")

    for bar, count in zip(bars, counts.values):
        ax.annotate(f"{count}", xy=(bar.get_x() + bar.get_width() / 2, count), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom")

    ax.set_ylabel("Number of Students")
    ax.set_xlabel("Status")
    ax.set_title("Student Performance Status")
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out