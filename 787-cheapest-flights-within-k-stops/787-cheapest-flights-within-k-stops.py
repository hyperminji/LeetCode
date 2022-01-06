#k개의 경유지 이내에 도착해야함
#우선순위큐에 추가할때 k이내일 때만 경로를 추가한다.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #src:출발지 dst:도착지 k:경유지 개수
        #flights[i] = [from_i, to_i, price_i]
        
        #weight: 해당 노드를 방문했던 경로의 (price, k)저장
        graph = collections.defaultdict(list)
        weight = [(sys.maxsize, k)]*n
        
        #그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v,w))
            
        #큐변수  [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, k)]
        
        #우선순위 큐 최솟값 기준 , 도착점 까지의 최소 비용 판별
        while Q:
            price, node, time = heapq.heappop(Q)
                        
            if node == dst:
                return price
            
            if time >= 0:
                for v,w in graph[node]:
                    alt = price + w
                    #alt < weight[v][0]:  push할 노드의 price < 해당 노드 weight의 price  
                    #time-1 >= weight[v][1]:   push할 노드의 time >=해당 노드 weight의 time
                    if alt < weight[v][0] or time-1 >= weight[v][1]:
                        weight[v] = (alt, time-1)
                        heapq.heappush(Q,(alt, v, time-1))
        return -1
        
        