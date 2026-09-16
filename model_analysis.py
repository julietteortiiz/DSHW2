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
        y += coef * (x ** count)
        count += 1
    return y

def calculate_residuals(
    x_values: Sequence[Number],
    y_values: Sequence[Number],
    coefficients: Sequence[float],
) -> list[float]:
    """Return observed-minus-predicted residuals."""
    residuals = list()
    i = 0
    for x in x_values:
        pred_y = calculate_y(x, coefficients)
        residuals.append(y_values[i] - pred_y)
        i += 1
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
    axes.scatter(x_values, y_values, label = label, color = color)
    axes.set_xlabel("Year")
    axes.set_ylabel("Sea Ice Extent (mil of km^2)")

    

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
    x = np.linspace(x_start, x_end, 100)
    y = calculate_y(x, coefficients)
    axes.plot(x,y, label = label, color=color)
    axes.set_xlabel("Year")
    axes.set_ylabel("Sea Ice Extent (mil of km^2)")
    
    

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
    data1979 = read_in_data("data/sea_ice_1979-2012.csv", x_type=["int", "float"])
    

    #split into x and y values
    x_values = data1979[0]
    y_values = data1979[1]
    fig1, axs = plt.subplots()
    plot_scatter(axs, x_values, y_values, label = "Initial Data", color = "Blue")
    axs.set_title("1979 Original Data")
    save_figure(fig1, "part1.pdf")

    

    #Calculate Y
    x_np = np.array(x_values)
    deg1 = calculate_y(x_np, DEGREE_1_COEFFICIENTS)
    fig2, axs = plt.subplots()
    plot_polynomial(axs, x_values[0], x_values[len(x_values)-1], DEGREE_1_COEFFICIENTS, label = "Degree 1 Polynomial", color = "Blue")
    axs.set_title("1979 Polynomial 1st Degree")
    save_figure(fig2, "part2_deg1.pdf")

    deg2 = calculate_y(x_np, DEGREE_2_COEFFICIENTS)
    fig3, axs = plt.subplots()
    plot_polynomial(axs, x_values[0], x_values[len(x_values)-1], DEGREE_2_COEFFICIENTS, label = "Degree 2 Polynomial", color = "Blue")
    axs.set_title("1979 Polynomial 2nd Degree")
    save_figure(fig3, "part2_deg2.pdf")

    #Calculate Regressions + Plot Them
    r1 = calculate_residuals(x_values, y_values, DEGREE_1_COEFFICIENTS)
    r2 = calculate_residuals(x_values, y_values, DEGREE_2_COEFFICIENTS)

    fig4, axs = plt.subplots()
    axs.set_title("1979 Polynomial 1st Degree Residuals")
    plot_scatter(axs, x_values, r1, label="Residuals for Degree1", color = "Blue")
    save_figure(fig4, "part2_residuals1.pdf")
    
    fig5, axs = plt.subplots()
    axs.set_title("1979 Polynomial 2nd Degree Residuals")
    plot_scatter(axs, x_values, r2, label="Residuals for Degree2", color = "Blue")
    save_figure(fig4, "part2_residuals2.pdf")

if __name__ == "__main__":
    main()

    