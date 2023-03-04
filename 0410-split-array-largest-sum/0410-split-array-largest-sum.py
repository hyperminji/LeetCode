class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        while low < high:
            mid = (low+high)//2
            total = 0
            count = 1
            for num in nums:
                if total+num <= mid:
                    total += num
                else:
                    total = num
                    count+=1
            if count > k:
                low = mid+1
            else:
                high = mid
        return high
        