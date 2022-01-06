class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(cansum, index, path):
            #음수이거나 0인 경우 종료
            if cansum < 0:
                return
            if cansum == 0: #종료 조건을 만족할 수 없기 때문에 무한탐색이 되어버린다
                result.append(path)
                return
            
            #재귀
            for i in range(index, len(candidates)):
                dfs(cansum-candidates[i],i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return result
                
        
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        def finder(candidates, target, t):
            if not target:
                answer.append(t)
                return 
            for i, num in enumerate(candidates):
                if target >= num:
                    finder(candidates[i:], target - num, t + [num])
                else:
                    break
        finder(candidates, target, [])
        return answer
'''
        