class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1=0
        s2=0
        for i in range(len(nums)):
            s1+=i+1
            s2+=nums[i]
        diff=s1-s2
        if diff==0:
            return 0
        else:
            return abs(diff)
                