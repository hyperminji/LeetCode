class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:#범위 벗어나면 예외처리
            return 0
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
        