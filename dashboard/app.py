import streamlit as st
import pandas as pd

st.title("Cricket Data Analytics Dashboard")

df = pd.read_csv("data/processed/cleaned_cricket_data.csv")

st.subheader("Player Data")

st.dataframe(df)

st.subheader("Runs Chart")

st.bar_chart(df.set_index("player")["runs"])
