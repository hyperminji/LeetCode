#bfs
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        direct = set()
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            direct.add((u,v))
            
        queue = collections.deque()
        queue.append(0)
        visited = [0]*n
        visited[0] = 1
        count = 0
        
        while queue:
            node = queue.popleft()
            for near in graph[node]:
                if not visited[near]:
                    if (near, node) not in direct:
                        count = count+1
                    visited[near] = 1
                    queue.append(near)
        return count
        
        