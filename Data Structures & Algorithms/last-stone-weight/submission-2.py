import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        """ 
        pop from the max heap, compare vals insert into heap then call 
        heapify
        reat unti we cant pop again
        """
        #i=heapq.heappop_max(stones)
        #j=heapq.heappop_max(stones)

        
        while len(stones)>1:
            x=heapq.heappop_max(stones)
            y=heapq.heappop_max(stones)
            #print("x=",x)
            #print("y=",y)
            if x==y:
                if len(stones)==0:
                    return 0
            elif y<x:
                x=x-y
                heapq.heappush(stones,x)
            elif y>x:
                y=y-x
                heapq.heappush(stones,y)
            heapq.heapify_max(stones)
        return heapq.heappop_max(stones)
        

