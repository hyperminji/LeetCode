#유클리드거리 추출 -> 크기가 작은 순으로 추출 -> 우선순위 큐로 k번 출력
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        #유클리드 거리
        for (x,y) in points:
            dist = x**2+y**2
            heapq.heappush(heap, (dist,x,y))
            
            
        #k번
        result = []
        for _ in range(k):
            (dist,x,y) = heapq.heappop(heap)
            result.append((x,y))
        return result
        