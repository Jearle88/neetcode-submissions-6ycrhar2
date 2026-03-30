class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        r=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                idx=stack.pop()
                days=i-idx
                r[idx]=days

            
            stack.append(i)
        return r