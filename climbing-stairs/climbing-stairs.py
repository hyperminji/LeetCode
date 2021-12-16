class Solution:
    def climbStairs(self, n: int) -> int:
        #n= 총계단의 개수, 1개 또는 2개만 올라갈 수 있음
        #얼마나 많은 경우의 수???
        #피보나치, dp
        if n<2:
            return 1
        
        i = 2
        dp ={0:1, 1:1}
        
        while i < n+1:
            dp[i] = dp[i-1] + dp[i-2]
            i = i+1

        return dp[n]