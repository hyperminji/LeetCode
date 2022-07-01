class Solution:
    def canJump(self, nums: List[int]) -> bool:
        point= 0
        for i,j in enumerate(nums):
            if point < i :
                return False
            point = max(point, i+j)
        return True
        