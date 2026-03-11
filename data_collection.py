import requests
import pandas as pd

def fetch_cricket_data():
    
    data = {
        "player": ["Virat Kohli", "Rohit Sharma", "Joe Root", "Steve Smith"],
        "runs": [12000, 10000, 9000, 8500],
        "matches": [250, 230, 220, 210],
        "average": [57.5, 49.2, 50.1, 52.3]
    }

    df = pd.DataFrame(data)
    df.to_csv("data/raw/cricket_matches.csv", index=False)

if __name__ == "__main__":
    fetch_cricket_data()
