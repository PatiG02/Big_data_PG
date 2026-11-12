import sys

current_key = None
total_cnt = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    zone, dist, cnt = parts[0], parts[1], int(parts[2])
    key = (zone, dist)
    
    if current_key == key:
        total_cnt += cnt
    else:
        if current_key is not None:
            print(f"{current_key[0]}\t{current_key[1]}\t{total_cnt}")
        current_key = key
        total_cnt = cnt

if current_key is not None:
    print(f"{current_key[0]}\t{current_key[1]}\t{total_cnt}")
