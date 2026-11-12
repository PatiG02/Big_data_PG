import pandas as pd

df = pd.read_parquet('/data/yellow_tripdata_2024-01.parquet')

# Lżejsza agregacja zamiast sortowania
agg_res = df.groupby(["PULocationID", "DOLocationID"])["trip_distance"].agg(["count", "mean"])

print(f"Liczba grup: {len(agg_res)}")
print("3 najliczniejsze pary stref:")
print(agg_res.sort_values(by="count", ascending=False).head(3))
