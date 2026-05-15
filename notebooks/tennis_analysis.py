import pandas as pd

# CSV-Datei laden
df = pd.read_csv("data/tennis_players.csv")

# Daten anzeigen
print("Tennis Players Dataset:")
print(df)

# Durchschnittliches Ranking berechnen
average_ranking = df["Ranking"].mean()

print("\nAverage Ranking:")
print(average_ranking)

# Spieler mit den meisten Titeln
top_player = df.loc[df["Titles"].idxmax()]

print("\nPlayer with most titles:")
print(top_player)
