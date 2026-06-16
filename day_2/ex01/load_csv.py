import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        csv = pd.read_csv(path)
    except FileNotFoundError:
        print("Invalid file")
        return
    except UnicodeDecodeError:
        print("Invalid start byte")
        return
    print(csv)
    return csv

