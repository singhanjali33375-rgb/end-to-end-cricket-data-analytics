import pandas as pd

def clean_data():

    df = pd.read_csv("data/raw/cricket_matches.csv")

    df.dropna(inplace=True)

    df["average"] = df["average"].round(2)

    df.to_csv("data/processed/cleaned_cricket_data.csv", index=False)

if __name__ == "__main__":
    clean_data()
