class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        res=0
        sign=1
        num=0
        for i in s:                             
            if i.isdigit():
                num=num*10+int(i)
            elif i=="+":
                res=res+sign*num
                sign=1
                num=0
            elif i=="-":
                res=res+sign*num
                sign=-1
                num=0
            elif i=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif i==")":
                res=res+sign*num
                num=0
                res=res*stack.pop()
                res=res+stack.pop()
        return res+sign*num


        
        