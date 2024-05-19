class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        dp = set([0])
        target = total//2

        for num in nums:
            nextDp = dp.copy()
            for val in dp:
                if val+num==target:
                    return True
                elif val+num<target:
                    nextDp.add(val+num)
            dp = nextDp
            
        return False