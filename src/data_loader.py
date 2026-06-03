import pandas as pd


def load_data(file_path):

    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    df["Date"] = pd.to_datetime(df["Date"])

    df.sort_values("Date", inplace=True)

    df.reset_index(drop=True, inplace=True)

    df.fillna(0, inplace=True)

    print("\n===== DATA LOADED SUCCESSFULLY =====")
    print(f"Rows : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df