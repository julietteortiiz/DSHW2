"""HW02: compare polynomial models for climate and toy regression data."""

from pathlib import Path
from typing import Literal, Sequence, Union

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
import csv

Number = Union[int, float]
XValue = Union[int, float]

DATA_DIR = Path("data")
FIGURES_DIR = Path("figures")

DEGREE_1_COEFFICIENTS = [190.5038227644984, -0.09224446142042844]
DEGREE_2_COEFFICIENTS = [
    -15150.155305067638,
    15.283380627913214,
    -0.0038525745647042583,
]


def read_in_data(
    file_path: Union[str, Path],
    x_type: Literal["int", "float"],
) -> tuple[list[XValue], list[float]]:
    """Return the x- and y-columns from a two-column CSV file."""
    # TODO: Read each row, converting x according to x_type and y to float.
    data = [list(), list()]
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            x = int(line[0])
            y = float(line[1])
            data[0].append(x)
            data[1].append(y)
    return data
        



        


def calculate_y(
    x: Union[Number, np.ndarray],
    coefficients: Sequence[float],
) -> Union[float, np.ndarray]:
    """Evaluate a polynomial whose coefficients are constant-term first."""
    # TODO: Implement polynomial evaluation without a built-in polynomial helper.
    raise NotImplementedError


def calculate_residuals(
    x_values: Sequence[Number],
    y_values: Sequence[Number],
    coefficients: Sequence[float],
) -> list[float]:
    """Return observed-minus-predicted residuals."""
    # TODO
    raise NotImplementedError


def residual_sum_of_squares(residuals: Sequence[Number]) -> float:
    """Return the sum of the squared residuals."""
    # TODO
    raise NotImplementedError


def plot_scatter(
    axes: Axes,
    x_values: Sequence[Number],
    y_values: Sequence[Number],
    *,
    label: str,
    color: str,
) -> None:
    """Add labeled scatter data to axes."""
    # TODO
    raise NotImplementedError


def plot_polynomial(
    axes: Axes,
    x_start: float,
    x_end: float,
    coefficients: Sequence[float],
    *,
    label: str,
    color: str,
) -> None:
    """Add a polynomial curve to axes over the requested x-range."""
    # TODO: np.linspace is useful here.
    raise NotImplementedError


def plot_elbow(axes: Axes, rss_values: Sequence[Number]) -> None:
    """Plot polynomial degree against RSS."""
    # TODO
    raise NotImplementedError


def save_figure(figure: plt.Figure, filename: str) -> None:
    """Save a figure in FIGURES_DIR and close it."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    figure.tight_layout()
    figure.savefig(FIGURES_DIR / filename)
    plt.close(figure)


def main() -> None:
    """Run all required analyses and create the figures listed in the handout."""
    # TODO: Organize Parts 1--4 here. Keep calculations in the functions above.
    pass


if __name__ == "__main__":
    main()
    print(read_in_data("data/sea_ice_2013-2020.csv", x_type=["int", "float"]))