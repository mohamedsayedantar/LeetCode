class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mergedIntervals = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            i_start, i_end = intervals[i][0], intervals[i][1]
            if i_start <= end:
                end = max(i_end, end)
            else:
                mergedIntervals.append([start, end])
                start, end = i_start, i_end
        mergedIntervals.append([start, end])
        return mergedIntervals

        