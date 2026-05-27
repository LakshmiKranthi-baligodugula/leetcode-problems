class Solution:
    def maxDepth(self, s: str) -> int:
        max_d=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
                max_d=max(max_d,len(stack))
            elif stack and i==")":
                stack.pop()
        return max_d