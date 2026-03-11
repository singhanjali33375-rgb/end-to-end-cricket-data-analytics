import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_cricket_data.csv")

plt.bar(df["player"], df["runs"])

plt.title("Top Cricket Players Runs")

plt.xlabel("Player")

plt.ylabel("Runs")

plt.show()
