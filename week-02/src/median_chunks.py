import pandas as pd

# Seria do przechowania zliczeń wystąpień wartości (stan)
value_counts = pd.Series(dtype='int64')

# Zliczenie wartości trip_distance w kolejnych porcjach
for chunk in pd.read_csv('/data/yellow_tripdata_2024-01.csv', chunksize =1_000_000, usecols=['trip_distance']):
  counts = chunk['trip_distance'].value_counts()
  value_counts = value_counts.add(counts, fill_value=0)

# Sortowanie indeksu zunifikowanych wartości
value_counts = value_counts.sort_index()
total_rows = value_counts.sum()
half_rows = total_rows / 2

# Wyznaczanie mediany z sumy
cumsum = value_counts.cumsum()
median_val = cumsum[cumsum >= half_rows].index[0]

print(f"Dokładna mediana: {median_val}")
print(f"Liczba pozycji w przenoszonym stanie: {len(value_counts)}")
