class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        profit=0

        low=0
        high=1
        while high<len(prices):
            if prices[low]> prices[high]:
                low+=1
                high=low+1
            elif prices[high]-prices[low]> profit:
                profit=prices[high]-prices[low]
                high+=1
            else:
                high+=1

        return profit