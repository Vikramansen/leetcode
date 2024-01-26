class Solution:
    def merge(self, intervals):
        intervals.sort()
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        return merged_intervals