class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        for i in range(1, length):
            result[i] = result[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result