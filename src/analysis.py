import numpy as np


def add_features(df):

    df["Daily Return"] = df["Close"].pct_change()

    df["MA20"] = df["Close"].rolling(window=20).mean()

    df["MA50"] = df["Close"].rolling(window=50).mean()

    df["Volatility"] = (
        df["Daily Return"]
        .rolling(window=20)
        .std()
    )

    return df


def stock_insights(df):

    best_day = df.loc[df["Daily Return"].idxmax()]

    worst_day = df.loc[df["Daily Return"].idxmin()]

    print("\n===== STOCK INSIGHTS =====")

    print("\nBest Gain Day")
    print(best_day[["Date", "Daily Return"]])

    print("\nWorst Loss Day")
    print(worst_day[["Date", "Daily Return"]])

    print(
        f"\nAverage Return : "
        f"{df['Daily Return'].mean():.4f}"
    )

    print(
        f"Risk : "
        f"{df['Daily Return'].std():.4f}"
    )

    print(
        f"Average Volatility : "
        f"{df['Volatility'].mean():.4f}"
    )