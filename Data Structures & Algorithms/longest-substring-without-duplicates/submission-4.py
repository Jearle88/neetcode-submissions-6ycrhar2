class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        sett=set()
        longest=0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l+=1
         
            w=(i-l)+1
            longest=max(longest,w)  
            sett.add(s[i])     
        return longest
