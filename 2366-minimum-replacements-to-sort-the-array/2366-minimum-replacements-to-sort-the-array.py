class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums) 
        operations = 0  
        prev_value = nums[n - 1] 

        
        for i in range(n - 2, -1, -1):
            if nums[i] > prev_value:
                k = (nums[i] + prev_value - 1) // prev_value
                operations += k - 1
                prev_value = nums[i] // k
            else:
                prev_value = nums[i]
        
        return operations  
