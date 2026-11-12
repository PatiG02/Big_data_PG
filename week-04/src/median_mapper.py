import sys

for line_no, line in enumerate(sys.stdin):
    if line_no == 0 and "VendorID" in line:
        continue
    parts = line.strip().split(',')
    if len(parts) > 7:
        try:
            float(parts[4])  # tylko walidacja, czy to poprawna liczba
            print(f"{parts[7]}\t{parts[4]}\t1")
        except ValueError:
            continue
