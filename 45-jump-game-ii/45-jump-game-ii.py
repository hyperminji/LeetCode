class Solution:
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        finalpoint = size -1
        
        curr = 0
        last_index = 0
        
        jumpcount = 0
        
        if size ==1:
            return 0
        
        for i in range(0, size):
            curr = max( curr, i+nums[i])
            
            if i == last_index:
                last_index = curr
                jumpcount += 1
                
                if curr >= finalpoint:
                    return jumpcount
        return jumpcount