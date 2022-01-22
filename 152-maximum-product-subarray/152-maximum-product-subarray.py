class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        small , large = 1, 1
        result = -float(inf)
        for n in nums:
            tmp_small = small
            small = min(n, n*small, n*large)
            large = max(n, n*tmp_small, n*large)
            result = max(result, large)
        return result
