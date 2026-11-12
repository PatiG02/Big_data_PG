import sys
import pandas as pd

# Pobranie liczby wierszy z argumentu wiersza poleceń (sys.argv[1])
nrows = int(sys.argv[1]) if len(sys.argv) > 1 else None

df = pd.read_csv('/data/yellow_tripdata_2024-01.csv', nrows=nrows)

mem_mb = df.memory_usage(deep=True).sum() / (1024**2)
print(f"Wiersze: {len(df)}, Zajetosc danych: {mem_mb:.2f} MB")
