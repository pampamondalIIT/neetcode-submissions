"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        Arrival = []
        Departure=[]
        n =0
        for i in intervals:
            Arrival.append(i.start)
            Departure.append(i.end)
            n+=1

        Arrival.sort()
        Departure.sort()
        i =0
        j =0
        platfroms = 0
        ans =0
        while i <n and j <n:
            if (Arrival[i]< Departure[j]):
                platfroms +=1
                ans = max(ans, platfroms)
                i +=1
            else:
                platfroms-=1
                j +=1
        return ans
        