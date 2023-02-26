class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ele = []
        
        for i in range(0 , len(grid)):
            for j in range(0 , len(grid[0])):
                ele.append(grid[i][j])
        
        k = k % len(ele)
        ele = ele[::-1]
        ele = ele[:k][::-1] + ele[k:][::-1]      
        
        k = 0
        for i in range(0 , len(grid)):
            for j in range(0 , len(grid[0])):
                grid[i][j] = ele[k]
                k += 1
        return grid