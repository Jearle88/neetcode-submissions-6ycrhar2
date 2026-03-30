"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        x=0
        y=x+1
        while y<len(intervals):
            if intervals[x].end>intervals[y].start:
                return False
            x+=1
            y+=1
        return True


        """
        for i in range(1,len(intervals)):
            sort_start.append(intervals[i.start])
        sort_start=sorted(sort_start)
        for j in range(1,len(intervals))
          """  
        




