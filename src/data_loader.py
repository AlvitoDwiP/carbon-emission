from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd


def load_processed_data(
    filename: str = "owid_co2_asean_2000_2024.csv",
    data_dir: str = "data/process",
    delimiter: str = ",",
    verbose: bool = True,
) -> pd.DataFrame:
    """Load a processed CSV from the project data directory.

    The function resolves paths safely for both project-root and notebook runs.
    """
    project_root = Path(__file__).resolve().parents[1]
    candidates = [
        Path(data_dir) / filename,
        Path("data/processed") / filename,
        Path(filename),
        project_root / data_dir / filename,
        project_root / "data/processed" / filename,
        project_root / filename,
    ]

    csv_path: Optional[Path] = next((p for p in candidates if p.exists()), None)

    if csv_path is None:
        looked = "\n- ".join(str(p) for p in candidates)
        raise FileNotFoundError(
            f"File '{filename}' tidak ditemukan. Lokasi yang dicek:\n- {looked}"
        )

    if verbose:
        print(f"Loaded: {csv_path}")

    return pd.read_csv(csv_path, delimiter=delimiter)

