from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:            
        stack = []
        total_water = 0   
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left=stack[-1]
                width=i-left- 1

                bounded_height = min(height[i], height[left]) - height[bottom]
                total_water += width* bounded_height
            stack.append(i)
           
            
        return total_water
