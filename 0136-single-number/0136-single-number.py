class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniquenum = 0
        for i in nums:
            uniquenum ^= i
        return uniquenum
        