"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n ==0:
            return True
        intervals.sort(key = lambda x:x.end)
        end = intervals[0].end
        
        for i in range(1,n):
            s = intervals[i].start
            e = intervals[i].end
            if end <= s:
                end = e
                continue
            else:
                return False

        return True
