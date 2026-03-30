class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip("!,#*?./")
        s=s.replace(" ", "")
        s=s.replace("'","")
        s=s.replace(",","")
        s=s.replace(":","")
        s=s.replace(";","")
        s=s.replace(".","")
        s=s.lower()
        #print(s)
        low=0
        high=len(s)-1
        while low<= high:
            if s[low]!= s[high]:
               # print("high",s[high])
                return False
            low+=1
            high-=1
        return True