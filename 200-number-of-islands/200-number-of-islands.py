class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            #섬이 아닌 경우 종료
            #좌표가 음수이거나 그리드의 범위를 벗어나는 경우, '0'인 경우
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] !='1':
                return
        
            grid[i][j] = 0  #좌표 초기화
        
            #동서남북 탐색
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        count = 0
    
        for i in range(len(grid)):  #그리드의 범위 안에서 4
            for j in range(len(grid[0])): #그리드의 세로 범위 5
                if grid[i][j]=='1': #좌표의 값이 1이라면 
                    dfs(i,j)  #섬 탐색
                    count +=1 #탐색완료 했으므로 섬 개수 증가
        return count
        
        