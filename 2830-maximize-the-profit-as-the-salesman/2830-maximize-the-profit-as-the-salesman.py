class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        minHeap = []
        amount = 0
        result = 0
        for start, end, gold in offers:
            while minHeap and minHeap[0][0] < start:
                amount = max(amount, heapq.heappop(minHeap)[1])
            heapq.heappush(minHeap, (end, amount + gold))
            result = max(result, amount + gold)
        return result