class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        low=0
        high=low+1
        longest=" "
        tmp=s[low]
        while high<= len(s)-1:
            if s[high] not in tmp:
                tmp=tmp+s[high]
                high+=1
            else:
                if len(tmp)>len(longest):
                    longest=tmp
                low+=1
                high=low+1
                tmp=s[low]
        if len(tmp)>len(longest):
            longest=tmp
        #print(longest)
        return len(longest)
