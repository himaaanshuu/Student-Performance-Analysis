from pathlib import Path
from typing import Union

import matplotlib
import matplotlib.pyplot as plt


def plot_attendance_vs_marks(df, out_path: Union[str, Path] = None) -> Path:
    """Compact, environment-independent plotter.

    - Saves a scatter plot of `attendance` vs `average_marks`.
    - If `out_path` is not provided it writes to `outputs/charts/attendance_vs_marks.png`
      at the repository root (computed relative to this file).
    - Uses the non-interactive Agg backend so it works on headless systems.

    Returns the Path to the created file (Path object). If required columns are
    missing, the function returns the intended output path but writes nothing.
    """
    repo_root = Path(__file__).resolve().parents[2]
    out = Path(out_path) if out_path is not None else repo_root / "outputs" / "charts" / "attendance_vs_marks.png"
    out.parent.mkdir(parents=True, exist_ok=True)

    if "attendance" not in df.columns or "average_marks" not in df.columns:
        return out

    # Ensure a non-interactive backend for headless environments
    try:
        matplotlib.use("Agg")
    except Exception:
        pass

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df["attendance"], df["average_marks"], alpha=0.7)
    ax.set_xlabel("Attendance")
    ax.set_ylabel("Average Marks")
    ax.set_title("Attendance vs Average Marks")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig(out)
    plt.close(fig)
    return out
import matplotlib.pyplot as plt

def plot_attendance_vs_marks(df):
    plt.figure()
    plt.scatter(df["attendance"], df["average_marks"])
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Marks")
    plt.title("Attendance vs Performance")
    plt.savefig("outputs/charts/attendance_vs_marks.png")
    plt.close()