class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp[i][j]  equal case: word1[:i+1], word2[:j+1]  ==> dp[i][j]
        #other case , find min  
        #delete: dp[i+1][j+1] = dp[i][j+1]+1  (word1[:i], word2[:j+1]// word1[i])
        #insert: dp[i+1][j+1] = dp[i+1][j]+1
        #replace: dp[i+1][j+1] = dp[i][j]+1
        #if word1[i]==word2[j]일때 dp[i+1][j+1] = dp[i][j] else min(delete, insert, replace)+1
        
        m,n = len(word1), len(word2)
        dp = [list(range(n+1))] + [[r+1]+[0]*n for r in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j] if word1[i] == word2[j] else min(dp[i][j], dp[i+1][j], dp[i][j+1])+1
                                
        return dp[m][n]
        