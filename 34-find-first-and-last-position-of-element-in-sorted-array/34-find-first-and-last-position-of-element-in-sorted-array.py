class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        reverse = nums[::-1]
        if target in nums:
            result.append(nums.index(target))
            i = reverse.index(target)+1
            result.append(len(nums)-i)
        else:
            return (-1,-1)
        
        return result
            
        
                
            
        