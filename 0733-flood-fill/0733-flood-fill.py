from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original=image[sr][sc]
        if original==color:
            return image
        q=deque([(sr,sc)])
        while q:
            r,c=q.popleft()
            if(0<=r<len(image)) and (0<=c<len(image[0])) and image[r][c]==original:
                image[r][c]=color
                q.append([r+1,c])
                q.append([r-1,c])
                q.append([r,c+1])
                q.append([r,c-1])
        return image
