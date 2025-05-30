import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[
    (df["value"] > df.quantile(0.025)["value"])
    & (df["value"] < df.quantile(0.975)["value"])
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=[12.8, 4.8])
    ax.plot(df.index, df["value"], "r")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df.resample("ME").mean()
    df_bar["Year"], df_bar["Month"] = df_bar.index.year, df_bar.index.month_name()
    df_bar = df_bar.pivot_table(values="value", index="Year", columns="Month")
    df_bar = df_bar[
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
    ]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=[9.6, 7.2])
    df_bar.plot.bar(ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6.4 * 2 * 1.5, 4.8 * 1.5])

    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        hue="year",
        palette=["tab:blue", "tab:orange", "tab:green", "tab:red"],
        legend=False,
        ax=ax1,
    )
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        hue="month",
        order=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        legend=False,
        ax=ax2,
    )
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
