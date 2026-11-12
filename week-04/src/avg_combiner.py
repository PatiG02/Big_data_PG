import sys

current_zone = None
total_dist = 0.0
count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 2:
        continue
    zone, dist = parts[0], float(parts[1])
    if current_zone == zone:
        total_dist += dist
        count += 1
    else:
        if current_zone is not None and count > 0:
            print(f"{current_zone}\t{total_dist/count:.4f}")
        current_zone = zone
        total_dist = dist
        count = 1

if current_zone is not None and count > 0:
    print(f"{current_zone}\t{total_dist/count:.4f}")
