def removeOuter(S):
        # Code here
        stack=[]
        res=""
        for i in S:
            
            if i=='(':
                if(len(stack))>0:
                    res+=i
                stack.append(i)
            else:
                if len(stack)>1:
                    res=res+i
                stack.pop() 
        return res  
s=input()
print(removeOuter(s))
