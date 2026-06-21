class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        start = intervals[0][0]
        end = intervals[0][1]
        n = len(intervals)
        remove = 0
        for i in range(1,n):
            s = intervals[i][0]
            e = intervals[i][1]
            if end <= s:
                end = e
                continue
            else:
                remove +=1

        return remove
        