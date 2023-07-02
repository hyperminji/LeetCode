class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsum = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (numsum - leftsum - x):
                return i
            leftsum += x
        return -1
        