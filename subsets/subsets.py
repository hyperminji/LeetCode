class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[]]
        
        for i in nums:
            result = result + [current + [i] for current in result]
            
        return result