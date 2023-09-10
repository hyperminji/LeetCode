class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        o = 0
        t = 0
        for num in nums:
            o = (o ^ num) & ~t
            t = (t ^ num) & ~o
        return o
        