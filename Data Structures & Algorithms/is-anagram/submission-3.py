class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #d1={}
        #d2={}
        if len(s)!= len(t):
           return False
        
        for letter in t:
            if letter not in s:
                return False
            s=s.replace(letter, '1', 1)
        #print(s)
        return True