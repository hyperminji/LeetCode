class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        answer = nums[len(nums)//2]
        return answer