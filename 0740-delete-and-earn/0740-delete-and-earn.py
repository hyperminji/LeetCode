class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        t= [0]*(max(nums)+1)
        
        for n in nums:
            t[n] += n
            
        dp = [0]*len(t)
        dp[1] = t[1]
        
        for i in range(2, len(t)):
            dp[i] = max(t[i]+ dp[i-2],dp[i-1])
            
        return dp[len(t)-1]
        
        
        