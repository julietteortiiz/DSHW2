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
    RSS = 0
    for residual in residuals:
        RSS += residual ** 2
    return RSS



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
    #PART1: Read In Data, convert to correct type
    data1979 = read_in_data("data/sea_ice_1979-2012.csv", x_type=["int", "float"])
    
    #split into x and y values
    x_values = data1979[0]
    y_values = data1979[1]
    fig1, axs = plt.subplots()
    plot_scatter(axs, x_values, y_values, label = "Initial Data", color = "Blue")
    axs.set_title("1979 Original Data")
    save_figure(fig1, "part1.pdf")

    

    #PART 2: Calculate Y
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
    save_figure(fig5, "part2_residuals2.pdf")

    #PART3
    data2013 = read_in_data("data/sea_ice_2013-2020.csv", x_type=["int", "float"])
    x_values_2013 = data2013[0]
    y_values_2013 = data2013[1]

    fig6, axs = plt.subplots()
    plot_polynomial(axs, 1979, 2012, DEGREE_1_COEFFICIENTS, label = "Degree 2 Polynomial", color = "Blue")
    plot_polynomial(axs, 2013, 2020, DEGREE_1_COEFFICIENTS, label = "Degree 2 Polynomial", color = "Red")
    axs.set_title("1979 and 2013 Degree 1")
    save_figure(fig6, "part3_pred1.pdf")

    fig7, axs = plt.subplots()
    plot_polynomial(axs, 1979, 2012, DEGREE_2_COEFFICIENTS, label = "Degree 2 Polynomial", color = "Blue")
    plot_polynomial(axs, 2013, 2020, DEGREE_2_COEFFICIENTS, label = "Degree 2 Polynomial", color = "Red")
    axs.set_title("1979 and 2013 Degree 2")
    save_figure(fig7, "part3_pred2.pdf")

    #PART4 - CHOOSING POLYNOMIAL DEGREE

    
    POLYNOMIAL_COEFFICIENTS = [
    #[1.13010595],
    [2.4464070947147207, -2.816353589568698],
    [2.522610178119313, -3.27003073191282, 0.4743087284609393],
    [1.2231425230496584, 10.649616212253513, -34.083679747347574, 23.590230897814727],
    [0.8075214798200756, 17.32934850900337, -62.32907523274797, 66.75220156315058, -21.61184507602993],
    [1.1537400009153576, 9.784042834672174, -14.963934203443742, -54.05134690879839, 111.9406595086277, -53.20467363235635],
    [1.6031281515537332, -2.212955964351817, 87.09165569133722, -440.6384252637192, 832.5418657076268, -698.5859135919, 221.439066525518],
    [1.0048620515132924, 17.4112052205856, -133.45588391947206, 713.2351017847259, -2320.831952624806, 3938.208550304347, -3249.3507974432723, 1036.2869129041017],
    [0.8889729225247591, 21.927863684690806, -196.3956341264095, 1135.1023058754872, -3863.15628401735, 7177.078002707203, -7143.712758937181, 3524.932857125692, -654.5246542101304],
    [6.455577860121968, -214.55025432038786, 3518.6484115354933, -28016.264919570815, 126197.74461140906, -343436.25785927917, 574211.0815161027, -575789.2765246094, 317309.99905972165, -73803.67907566673],
    [5.571266255808752, -173.07147738443035, 2771.613686468927, -21023.423222254118, 87668.04317051847, -210606.67961073387, 280101.8712329003, -158297.13764038868, -49517.323077016044, 107648.64893355407, -38599.19918692205],
]
    regression_x = list()
    regression_y = list()
    with open("data/regression_train.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            regression_x.append(float(line[0]))
            regression_y.append(float(line[1]))
        

    i = 1
    for degree in POLYNOMIAL_COEFFICIENTS:
        fig, axs = plt.subplots()
        plot_polynomial(axs, regression_x[0], regression_x[len(regression_x)-1], degree, label = "training", color = "blue")
        axs.set_title("Training on " + str(i) + " Degree")
        save_figure(fig, "part4_deg" + str(i) + ".pdf")
        i += 1




    



if __name__ == "__main__":
    main()

    