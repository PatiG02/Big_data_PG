import pandas as pd

# Wczytanie danych referencyjnych z Parquetu
df = pd.read_parquet('/data/yellow_tripdata_2024-01.parquet')

# Obliczenie statystyk w pandas
ref = df.groupby('PULocationID')['trip_distance'].agg(
    count='count',
    mean='mean',
    median='median'
).reset_index()
ref['PULocationID'] = ref['PULocationID'].astype(str)

# Wczytanie wyników z klastra Z1 (średnia) i Z3 (mediana)
mr_mean = pd.read_csv('/out/z1-mean.tsv', sep='\t', names=['zone', 'mr_mean', 'mr_count'], dtype={'zone': str})
mr_median = pd.read_csv('/out/z3-median.tsv', sep='\t', names=['zone', 'mr_median', 'mr_count_med', 'mr_unique'], dtype={'zone': str})

# Połączenie po numerze strefy
merged = pd.merge(ref, mr_mean, left_on='PULocationID', right_on='zone')
merged = pd.merge(merged, mr_median, on='zone')

# Porównanie wyników
diff_count = (merged['count'] != merged['mr_count']).sum()
max_mean_diff = (merged['mean'] - merged['mr_mean']).abs().max()
diff_median = (merged['median'] - merged['mr_median']).abs().gt(0.001).sum()

print("===== WERYFIKACJA POPRAWNOŚCI WYNIKÓW (Z4) =====")
print(f"Liczba stref po obu stronach         : {len(merged)}")
print(f"Zgodność liczby kursów (różnice != 0): {diff_count}")
print(f"Największa różnica średnich          : {max_mean_diff:.5f}")
print(f"Liczba różnych median                : {diff_median}")

# Analiza błędnego wariantu Z2 (z2-avg) - uwzględniamy wszystkie 3 kolumny z pliku
mr_avg = pd.read_csv('/out/z2-avg.tsv', sep='\t', names=['zone', 'mr_avg_mean', 'mr_avg_groups'], dtype={'zone': str})
merged_avg = pd.merge(ref, mr_avg, left_on='PULocationID', right_on='zone')
merged_avg['diff'] = (merged_avg['mean'] - merged_avg['mr_avg_mean']).abs()

diff_gt_001 = (merged_avg['diff'] > 0.01).sum()
print("\n----- Analiza wariantu z2-avg -----")
print(f"Liczba stref różniących się o > 0.01 mili: {diff_gt_001} z {len(merged_avg)}")

top10_diff = merged_avg.sort_values(by='diff', ascending=False).head(10)
print("\n10 największych różnic w z2-avg:")
for _, row in top10_diff.iterrows():
    print(f"Strefa {row['zone']:>3}: kursów={row['count']:>6}, pandas={row['mean']:.4f}, z2-avg={row['mr_avg_mean']:.4f}, diff={row['diff']:.4f}")
