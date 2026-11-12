import sys

for line_no, line in enumerate(sys.stdin):
    if line_no == 0 and "VendorID" in line:
        continue
    parts = line.strip().split(',')
    if len(parts) > 7:
        try:
            pu_location = parts[7]
            trip_distance = float(parts[4])
            print(f"{pu_location}\t{trip_distance}")
        except ValueError:
            continue
