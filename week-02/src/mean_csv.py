import pandas as pd

df = pd.read_csv('/data/yellow_tripdata_2024-01.csv')

print(f"Liczba wierszy: {len(df)}")
print(f"Sredni dystans: {df['trip_distance'].mean()}")
