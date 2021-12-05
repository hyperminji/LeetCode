class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs?
        count = 0  # island count
        
        def dfs(i,j):
            if i<0 or i >=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
                return
            grid[i][j]='0'
            #4방향
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count = count+1
        return count
            
        