import pandas as pd

chunk_size = 1_000_000
chunk_means = []
total_sum = 0.0
total_count = 0

for i, chunk in enumerate(pd.read_csv('/data/yellow_tripdata_2024-01.csv', chunksize=chunk_size)):
    c_len = len(chunk)
    c_mean = chunk['trip_distance'].mean()
    c_median = chunk['trip_distance'].median()
    
    chunk_means.append(c_mean)
    total_sum += chunk['trip_distance'].sum()
    total_count += c_len
    
    print(f"Porcja {i+1}: wierszy={c_len}, srednia={c_mean:.4f}, mediana={c_median:.2f}")

mean_a = sum(chunk_means) / len(chunk_means)
mean_b = total_sum / total_count

print(f"Srednia (a - ze srednich porcji): {mean_a:.4f}")
print(f"Srednia (b - z sumy dystansow i liczby wierszy: {mean_b:.4f}")
