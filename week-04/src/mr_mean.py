"""List 4, Z1: mean trip distance per pickup zone, with a combiner, as ONE mrjob class.
Fill in the three methods. The logic is the same as in your sumcount_mapper.py,
sumcount_combiner.py and sumcount_reducer.py from list 3 (Z2).
"""
from mrjob.job import MRJob


class MeanDistance(MRJob):
    def mapper(self, _, line):
        # one CSV line; skip the header; yield zone, (distance, 1)
        if line.startswith("VendorID"):
            return
        parts = line.strip().split(',')
        if len(parts) > 7:
            try:
                zone = parts[7]
                distance = float(parts[4])
                yield zone, (distance, 1)
            except ValueError:
                pass

    def combiner(self, zone, states):
        # states: (sum, count) pairs of ONE zone; yield zone, (sum, count)
        total_sum = 0.0
        total_count = 0
        for s, c in states:
            total_sum += s
            total_count += c
        yield zone, (total_sum, total_count)

    def reducer(self, zone, states):
        # sum like the combiner, then yield zone, (mean rounded to 4 places, count)
        total_sum = 0.0
        total_count = 0
        for s, c in states:
            total_sum += s
            total_count += c
        if total_count > 0:
            yield zone, (round(total_sum / total_count, 4), total_count)


if __name__ == "__main__":
    MeanDistance.run()
