class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        answer = [0] * len(nums)
        for i in nums:
            if i % 2 == 0:
                answer[left] = i
                left += 1
            else:
                answer[right] = i
                right -= 1
        return answer
        