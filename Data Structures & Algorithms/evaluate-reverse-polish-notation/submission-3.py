class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            # if oprator, pop the next 2 int on stack, add then put them back on stack
            if tokens[i] in '+-/*':
                val1=stack.pop()
                val2=stack.pop()
                #print("v1",val1)
                #print("v2",val2)
                if tokens[i]=="+":
                    stack.append(val1+val2)
                    #print("+")
                elif tokens[i]=="-":
                    stack.append(val2-val1)
                   # print("-")
                elif tokens[i]=="*":
                    #print("*")
                    stack.append(val2*val1)
                elif tokens[i]=="/":
                    #print("/")
                    if ((val1<0) and (val2<0))  or ((val1>0) and (val2>0)):
                        stack.append(abs(val2)//abs(val1))
                    else:
                        tmp=abs(val2)//abs(val1)
                        tmp=tmp*-1
                        stack.append(tmp)    
               # print(stack[-1])
            else:
                stack.append(int(tokens[i]))
        return stack[0]
                