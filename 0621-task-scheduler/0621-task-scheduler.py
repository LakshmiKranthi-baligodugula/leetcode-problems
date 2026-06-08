from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=Counter(tasks) #a=3 b=3
        max_heap=[]
        for count in d.values():
            heapq.heappush(max_heap,-count) #[-3,,-3ycle=n+1
        time=0
        while max_heap:
            temp=[]
            cycle=n+1
            while cycle>0 and max_heap:
                count=-heapq.heappop(max_heap) #making -ve to +ve
                count-=1
                time+=1
                if count>0:
                    temp.append(count)
                cycle-=1
            for count in temp:
                heapq.heappush(max_heap,-count)
            if max_heap:
                time=time+cycle
        return time
            
        

'''time=0
cycle=n-1     
heap=[-3,-3]
execute A
c=2
time=n+1
cycle=3-1=2
'''
        

        