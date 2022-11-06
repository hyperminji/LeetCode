class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        freq_heap = []
        
        for f in freq:
            heapq.heappush(freq_heap, (-freq[f],f))
            
        answer = list()
        
        for _ in range(k):
            answer.append(heapq.heappop(freq_heap)[1])
        return answer
        