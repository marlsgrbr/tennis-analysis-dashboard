import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel
st.title("🎾 Tennis Scouting Dashboard")

# Daten laden
df = pd.read_csv("data/atp_matches_2026.csv")

# Durchschnittliche Asses berechnen
average_aces = (
    df.groupby("winner_name")["w_ace"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Daten anzeigen
st.subheader("Top 10 Players by Average Aces")

st.dataframe(average_aces)

# Diagramm erstellen
fig, ax = plt.subplots(figsize=(10, 5))

average_aces.plot(kind="bar", ax=ax)

ax.set_title("Top 10 Players by Average Aces")
ax.set_xlabel("Player")
ax.set_ylabel("Average Aces")

plt.xticks(rotation=20)

# Diagramm anzeigen
st.pyplot(fig)
