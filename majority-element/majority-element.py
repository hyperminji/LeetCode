class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#첫번째 풀이
#        nums.sort()
#        answer = nums[len(nums)//2]
#        return answer
#두번째 풀이
        count = 0
        answer = None
        for n in nums:
            if count == 0:
                answer = n
            if n == answer:
                count = count +1
            else:
                count = count -1
        return answer