class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s_i=" "
        if_9=False
        i=len(digits)-1
        if digits[i]==9:
            prev=0
            #digits[i]=0
            #i=i-1    
            while (prev==0 ) and (i>0):
                if digits[i]==9:
                    digits[i]=0
                    prev=digits[i]
                else:
                    digits[i]+=1
                    prev=digits[i]
                    break                    
                i-=1
            if prev==0 :
                if digits[0]==9:   
                    digits[0]=0
                    digits.insert(0,1)
                else:
                    digits[0]=digits[0]+1
            return digits
        else:
            digits[i]+=1
            return digits
            
                
                
           

 