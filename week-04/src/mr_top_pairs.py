"""List 4, Z2: the ten most frequent (pickup zone, drop-off zone) pairs, in TWO steps.
Step 1 counts every pair. Step 2 gives all counts the same key, so ONE reducer sees them all.
Fill in the four methods; steps() is ready.
"""
import heapq

from mrjob.job import MRJob
from mrjob.step import MRStep


class TopPairs(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.emit_pair, combiner=self.sum_counts, reducer=self.sum_counts),
            MRStep(mapper=self.to_one_key, reducer=self.top_ten),
        ]

    def emit_pair(self, _, line):
        # skip the header; yield "PULocationID->DOLocationID", 1  (columns 7 and 8)
        if line.startswith("VendorID"):
            return
        parts = line.strip().split(',')
        if len(parts) > 8:
            pu_zone = parts[7]
            do_zone = parts[8]
            yield f"{pu_zone}->{do_zone}", 1

    def sum_counts(self, pair, counts):
        # yield pair, the sum of counts
        yield pair, sum(counts)

    def to_one_key(self, pair, n):
        # yield None, (n, pair)
        yield None, (n, pair)

    def top_ten(self, _, pairs):
        # heapq.nlargest(10, pairs) gives the ten largest (n, pair); yield pair, n
        for n, pair in heapq.nlargest(10, pairs):
            yield pair, n


if __name__ == "__main__":
    TopPairs.run()
