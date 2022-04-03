class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for lev in range(len(triangle)-2, -1,-1): #삼각형의 아래에서 시작 위로 이동
            for i in range(lev+1):
                #아래행의 동일한 인덱스 / 인덱스+1
                triangle[lev][i] += min(triangle[lev+1][i], triangle[lev+1][i+1]) 
        return triangle[0][0]
        