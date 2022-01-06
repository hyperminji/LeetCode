#최단경로, 다익스트라
#모든 노드가 신호를 받는데 걸리는 시간
#모든 노드에 도달할 수 있는지 여부
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        #그래프 인접 리스트 구성 u:기준노드 v:도착노드 w:도착시간 
        for u,v,w in times:
            graph[u].append((v,w))
            
        #Q=[(소요시간, 정점)]
        Q = [(0,k)]
        dist = collections.defaultdict(int)
        
        #우선순위 큐 min 기준으로 정점까지 최단경로 append
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q,(alt,v))
                    
        #모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1
    
        
        