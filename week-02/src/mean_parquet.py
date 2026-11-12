import pandas as pd

df = pd.read_parquet('/data/yellow_tripdata_2024-01.parquet')

print(f"Liczba wierszy: {len(df)}")
print(f"Sredni dystans: {df['trip_distance'].mean()}")

# Zajętość samych danych w RAM
mem_bytes = df.memory_usage(deep=True).sum()
print(f"Zajetosc danych w RAM: {mem_bytes / (1024**2):.2f} MB")
