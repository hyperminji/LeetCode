#sort 한다음에 k-1번째
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        answer = nums[k-1]
        return answer
        
        