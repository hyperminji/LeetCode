class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indexi = set()
        indexj = set()
        
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    indexi.add(i)
                    indexj.add(j)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if i in indexi or j in indexj:
                    matrix[i][j] = 0