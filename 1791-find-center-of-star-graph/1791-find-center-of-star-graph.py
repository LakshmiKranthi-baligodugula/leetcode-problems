from collections import deque
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        start=-1
        mx=0
        for node in graph:
            if len(graph[node])>mx:
                mx=len(graph[node]) 
                start=node
        q=deque([start])
        visited={start}
        while q:
            node=q.popleft()
            for neighbour in graph[node]:
                if neighbour not in  visited:
                    visited.add(neighbour)
                    q.append(neighbour)
        return start






        

        