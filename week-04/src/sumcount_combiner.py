import sys

current_zone = None
sum_dist = 0.0
sum_count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    zone, dist, cnt = parts[0], float(parts[1]), int(parts[2])
    if current_zone == zone:
        sum_dist += dist
        sum_count += cnt
    else:
        if current_zone is not None:
            print(f"{current_zone}\t{sum_dist}\t{sum_count}")
        current_zone = zone
        sum_dist = dist
        sum_count = cnt

if current_zone is not None:
    print(f"{current_zone}\t{sum_dist}\t{sum_count}")
