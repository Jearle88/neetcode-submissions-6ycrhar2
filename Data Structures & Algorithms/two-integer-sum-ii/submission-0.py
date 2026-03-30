class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while high< len(numbers) and (low<= high):
            tmp=numbers[high]+numbers[low]
            if tmp== target:
                return[low+1,high+1]
            elif tmp< target:
                low+=1
            elif tmp> target:
                high-=1
        
            