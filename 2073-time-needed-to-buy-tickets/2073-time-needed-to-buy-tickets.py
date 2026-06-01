from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append((i,tickets[i]))
        time=0
        while q:
            index,count=q.popleft()
            count=count-1
            time=time+1
            if index==k and count==0:
                return time

            if count>0:
                q.append((index,count))



    