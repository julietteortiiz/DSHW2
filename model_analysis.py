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
    x: Union[Number, np.ndarray], #indicates that x can be a scalar or numpy array
    coefficients: Sequence[float],
) -> Union[float, np.ndarray]:
    """Evaluate a polynomial whose coefficients are constant-term first."""
    # TODO: test for edge case
    y = coefficients[0]
    count = 1
    for coef in coefficients[1:]:
        print("Y: " + str(y))
        print("EQ: " + str(coef) + str(x) + "^" + str(count))
        y += coef * (x ** count)
        print("After Y: " + str(y))
        count += 1
    return y

def calculate_residuals(
    x_values: Sequence[Number],
    y_values: Sequence[Number],
    coefficients: Sequence[float],
) -> list[float]:
    """Return observed-minus-predicted residuals."""
    ydeg1 = calculate_y(x_values, DEGREE_1_COEFFICIENTS)
    residuals = list()
    for i in range(len(y_values)):
        residual = y_values[i] - ydeg1[i]
        residuals.append(residual)    
    return residuals


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
    axes.scatter(x_values, y_values)
    axes.set_title(label)
    axes.tick_params(labelcolor=color)

    

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
    #Read In Data, convert to correct type
    data2013 = read_in_data("data/sea_ice_2013-2020.csv", x_type=["int", "float"])
    print(data2013)
    

    #split into x and y values
    x_values = np.array(data2013[0])
    y_values = np.array(data2013[1])
    fig1, axs = plt.subplots()
    plot_scatter(axs, x_values, y_values, label = "Initial Data", color = "Blue")
    axs.set_xlabel("Year")
    axs.set_ylabel("Sea Ice %")
    save_figure(fig1, "Initial Data")
    

    #Calculating y with degree1 coefficients
    residuals1 = calculate_residuals(x_values, y_values, DEGREE_1_COEFFICIENTS)
    
    #Calculating y with degree2 coefficients
    residuals2 = calculate_residuals(x_values, y_values, DEGREE_2_COEFFICIENTS)


if __name__ == "__main__":
    main()

    