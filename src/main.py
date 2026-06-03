from data_loader import load_data

from analysis import (
    add_features,
    stock_insights
)

from visualization import (
    plot_closing_price,
    plot_moving_average,
    plot_volume,
    correlation_heatmap,
    plot_daily_return,
    plot_volatility
)


def main():

    df = load_data("data/stock_data.csv")

    df = add_features(df)

    stock_insights(df)

    print("\n===== DATASET INFO =====")
    print(df.info())

    print("\n===== SUMMARY STATISTICS =====")
    print(df.describe())

    # Graphs
    plot_closing_price(df)

    plot_moving_average(df)

    plot_volume(df)

    correlation_heatmap(df)

    plot_daily_return(df)

    plot_volatility(df)


if __name__ == "__main__":
    main()