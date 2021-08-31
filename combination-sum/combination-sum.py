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
        