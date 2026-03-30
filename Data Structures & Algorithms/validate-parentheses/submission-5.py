class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        #print("first",s[0])
        for i in range(len(s)):
            if s[i] in "[{(": 
                stack.append(s[i])
               # print(stack)
            elif len(stack)==0:
                return False
            elif s[i]=="]":    
                if stack.pop()!="[":
                    #print("-2",stack[-1])
                    return False
            elif s[i]=="}":
                if stack.pop()!="{":
                    #print("3")
                    return False
            elif s[i]==")":
                if stack.pop()!="(":
                    return False
        if len(stack)==0:
            return True
        else: 
            return False
       
            