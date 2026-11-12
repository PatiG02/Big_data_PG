import sys
from collections import defaultdict

current_zone = None
counts = defaultdict(int)

def process_zone(zone, counts_dict):
    sorted_dists = sorted(counts_dict.keys())
    total_trips = sum(counts_dict.values())
    unique_vals = len(sorted_dists)
    
    accum = 0
    med = 0.0
    
    if total_trips % 2 != 0:
        target = (total_trips + 1) // 2
        for d in sorted_dists:
            accum += counts_dict[d]
            if accum >= target:
                med = d
                break
    else:
        t1 = total_trips // 2
        t2 = t1 + 1
        m1, m2 = None, None
        for d in sorted_dists:
            accum += counts_dict[d]
            if m1 is None and accum >= t1:
                m1 = d
            if m2 is None and accum >= t2:
                m2 = d
                break
        med = (m1 + m2) / 2.0

    print(f"{zone}\t{med:.3f}\t{total_trips}\t{unique_vals}")

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    zone, dist_str, cnt_str = parts[0], parts[1], parts[2]
    try:
        dist, cnt = float(dist_str), int(cnt_str)
    except ValueError:
        continue
    
    if current_zone == zone:
        counts[dist] += cnt
    else:
        if current_zone is not None:
            process_zone(current_zone, counts)
        current_zone = zone
        counts = defaultdict(int)
        counts[dist] = cnt

if current_zone is not None:
    process_zone(current_zone, counts)
