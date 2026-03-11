import pandas as pd

def analyze_data():

    df = pd.read_csv("data/processed/cleaned_cricket_data.csv")

    top_player = df.sort_values(by="runs", ascending=False)

    print("Top Run Scorers")
    print(top_player)

if __name__ == "__main__":
    analyze_data()
