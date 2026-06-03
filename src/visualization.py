import matplotlib.pyplot as plt
import seaborn as sns


def plot_closing_price(df):

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["Date"],
        df["Close"],
        color="blue"
    )

    plt.title("Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Close Price")

    plt.show()


def plot_moving_average(df):

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["Date"],
        df["MA20"],
        label="MA20",
        color="orange"
    )

    plt.plot(
        df["Date"],
        df["MA50"],
        label="MA50",
        color="green"
    )

    plt.title("Moving Average")

    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()

    plt.show()


def plot_volume(df):

    plt.figure(figsize=(10, 5))

    plt.bar(
        df["Date"],
        df["Volume"],
        color="purple"
    )

    plt.title("Trading Volume")

    plt.xlabel("Date")
    plt.ylabel("Volume")

    plt.show()


def correlation_heatmap(df):

    plt.figure(figsize=(8, 5))

    sns.heatmap(
        df[
            [
                "Open",
                "High",
                "Low",
                "Close",
                "Volume"
            ]
        ].corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.show()


def plot_daily_return(df):

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["Date"],
        df["Daily Return"],
        color="red"
    )

    plt.title("Daily Return Trend")

    plt.xlabel("Date")
    plt.ylabel("Daily Return")

    plt.show()


def plot_volatility(df):

    plt.figure(figsize=(8, 5))

    volatility_data = [
        df["Volatility"].mean(),
        df["Volatility"].max(),
        df["Volatility"].min()
    ]

    labels = [
        "Average",
        "Maximum",
        "Minimum"
    ]

    plt.pie(
        volatility_data,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Volatility Distribution")

    plt.show()