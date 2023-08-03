class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        fresh_orange = 0
        
        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        count = 0
        while queue and fresh_orange > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == row or yy < 0 or yy == col:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    queue.append((xx, yy))
                    grid[xx][yy] = 2
                    fresh_orange -= 1
            count += 1
        return count if fresh_orange == 0 else -1
        