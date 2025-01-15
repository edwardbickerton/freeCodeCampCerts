import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col="Year")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df.index, df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    l1 = linregress(df.index, df["CSIRO Adjusted Sea Level"])
    x = np.arange(1880, 2051)
    ax.plot(
        x,
        l1.slope * x + l1.intercept,
        c="r",
    )

    # Create second line of best fit
    l2 = linregress(
        df[df.index >= 2000].index,
        df[df.index >= 2000]["CSIRO Adjusted Sea Level"],
    )
    x = np.arange(2000, 2051)
    ax.plot(
        x,
        l2.slope * x + l2.intercept,
        c="tab:orange",
    )

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
