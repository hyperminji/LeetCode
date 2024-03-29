class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(cansum, index, path):
            #음수or 0인 경우 종료
            if cansum < 0:
                return
            if cansum == 0: #종료 조건을 만족x 무한탐색
                result.append(path)
                return
            
            #재귀
            for i in range(index, len(candidates)):
                dfs(cansum-candidates[i],i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return result