class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        di = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        land1 = collections.deque()
        
        def dfs(x,y):
            for dx, dy in di:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy]==1:
                    grid[x+dx][y+dy] = 2
                    land1.append([x+dx, y+dy])
                    dfs(x+dx, y+dy)
        
        def findland1():
            for x in range(row):
                for y in range(col):
                    if grid[x][y]:
                        return dfs(x,y)
        findland1()
        
        stepblock = 0
        while land1:
            for _ in range(len(land1)):
                x,y = land1.popleft()
                for dx,dy in di:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<row and 0<=ny<col and grid[nx][ny] != 2:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            land1.append([nx,ny])
                        elif grid[nx][ny] == 1:
                            return stepblock
            stepblock += 1
        return stepblock
                
        
        