import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       # heapq.heapify_max(nums)
        h=[]
        
        for i in range(len(nums)):
            if len(h)<k:
                heapq.heappush(h,nums[i])
            elif nums[i]>h[0]:
                heapq.heappop(h)
                heapq.heappush(h,nums[i])
            
        return h[0]



        