class Solution:
    def intervalIntersection(self, intervals_a: List[List[int]], intervals_b: List[List[int]]) -> List[List[int]]:
        result = []
        i, j, start, end = 0, 0, 0, 1

        while i < len(intervals_a) and j < len(intervals_b):
            a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                               intervals_a[i][start] <= intervals_b[j][end]

            b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and \
                               intervals_b[j][start] <= intervals_a[i][end]

            if (a_overlaps_b or b_overlaps_a):
                result.append([max(intervals_a[i][start], intervals_b[j][start]), min(
                intervals_a[i][end], intervals_b[j][end])])

            if intervals_a[i][end] < intervals_b[j][end]:
                i += 1
            else:
                j += 1

        return result