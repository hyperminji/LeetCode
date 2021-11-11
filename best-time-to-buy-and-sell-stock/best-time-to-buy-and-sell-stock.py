class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        
        if len(prices) < 2:
            return result
        
        start_price = prices[0]
        
        for price in prices[1:]:
            start_price = min(price, start_price)
            result = max(result, price - start_price)
        return result

        