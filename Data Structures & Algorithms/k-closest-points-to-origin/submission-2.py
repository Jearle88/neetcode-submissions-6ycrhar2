import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        o1=0
        o2=0
        """ 
        itrarte through the list , calc distance betwwen all points
        and store in list, make that list a heap and pop the k amount of points
        to get the corfrect indicies, 
        store as tuples with 1 val being the index and other one being the distance

        """
        def dist(x1,y1,x2,y2):

            return (x1-x2)**2+(y1-y2)**2
        h=[]
        for i in range(len(points)):
            heapq.heappush(h, (dist(o1,o2,(points[i][0]),(points[i][1])),str(i)))
        res=[]
        
        for i in range(k):
           d1,d2= heapq.heappop(h)
           res.append((points[int(d2)]))
        return res



