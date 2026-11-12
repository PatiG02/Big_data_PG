import pandas as pd

df = pd.read_parquet('/data/yellow_tripdata_2024-01.parquet')

# Sortowanie przejazdów wewnątrz grup
res = df.groupby(["PULocationID", "DOLocationID"]).apply(
    lambda g: g.sort_values("trip_distance"), include_groups=False
)
print("Grupowanie i sortowanie zakończone pomyślnie.")
