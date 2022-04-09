from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que= deque()
        answer = []
        for i, curr in enumerate(nums):
            while que and nums[que[-1]] <= curr:
                que.pop()
            que.append(i)
            
            if que[0] == i - k:
                que.popleft()
            if i >= k-1:
                answer.append(nums[que[0]])
        return answer