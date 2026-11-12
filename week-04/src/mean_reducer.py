import sys

current_zone = None
total_distance = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    
    zone, dist_str = parts[0], parts[1]
    try:
        dist = float(dist_str)
    except ValueError:
        continue

    if current_zone == zone:
        total_distance += dist
        count += 1
    else:
        if current_zone is not None and count > 0:
            avg = total_distance / count
            print(f"{current_zone}\t{avg:.4f}\t{count}")
        current_zone = zone
        total_distance = dist
        count = 1

if current_zone is not None and count > 0:
    avg = total_distance / count
    print(f"{current_zone}\t{avg:.4f}\t{count}")
