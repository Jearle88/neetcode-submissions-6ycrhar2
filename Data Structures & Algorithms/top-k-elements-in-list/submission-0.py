class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        if len( nums)==1:
            return [nums[0]]
        #r=[]
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        top_k_keys = sorted(d, key=d.get, reverse=True)[:k]
          
        return   top_k_keys