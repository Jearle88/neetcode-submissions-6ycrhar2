class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z_count=0 
        product=1
        z_idx=-1
        for x in range(len(nums)):
            if nums[x]==0:
                z_count+=1
                z_idx=x
            else:
                product=nums[x]*product
       # products=[1]*len(nums)
        if z_count>1:
            return [0]*len(nums)
        if z_count==1:
            for y in range( len(nums)):
                if nums[y]!=0:
                    nums[y]=0
                else:
                    nums[y]=product            
            return nums
        for i in range(len(nums)):
         nums[i]=product//nums[i]
        return nums
            
