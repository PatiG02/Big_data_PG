import sys

current_zone = None
total_dist = 0.0
total_count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    zone, dist, cnt = parts[0], float(parts[1]), int(parts[2])
    if current_zone == zone:
        total_dist += dist
        total_count += cnt
    else:
        if current_zone is not None and total_count > 0:
            print(f"{current_zone}\t{total_dist/total_count:.4f}\t{total_count}")
        current_zone = zone
        total_dist = dist
        total_count = cnt

if current_zone is not None and total_count > 0:
    print(f"{current_zone}\t{total_dist/total_count:.4f}\t{total_count}")
