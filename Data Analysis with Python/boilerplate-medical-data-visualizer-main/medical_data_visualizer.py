import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = ((df["weight"] / ((df["height"] / 100) ** 2)) > 25).astype(int)

# 3
for column in ["cholesterol", "gluc"]:
    df.loc[df[column] == 1, column] = 0
    df.loc[df[column] > 1, column] = 1


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(
        id_vars=["id", "cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).count()

    # 7
    df_cat.reset_index(inplace=True)
    df_cat.rename(columns={"id": "total"}, inplace=True)

    # 8
    fig = sns.catplot(
        df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar"
    )

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[df["ap_lo"] <= df["ap_hi"]]
    for column in ["height", "weight"]:
        df_heat = df_heat.loc[
            (df_heat[column] >= df_heat[column].quantile(0.025))
            & (df_heat[column] < df_heat[column].quantile(0.975))
        ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f")

    # 16
    fig.savefig("heatmap.png")
    return fig
