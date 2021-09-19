class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #교차점
        tt= nums[0]
        rr= nums[0]
        
        while True:
            tt = nums[tt]
            rr = nums[nums[rr]]
            if tt == rr:
                break
                
            
        #입구
        tt = nums[0]
        while tt != rr:
            tt = nums[tt]
            rr = nums[rr]
        return rr