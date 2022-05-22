class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        
        def worker(ans, str):
            if str:
                for i in range(1, len(str)+1):
                    if str[:i] == str[:i][::-1]:
                        worker(ans+[str[:i]], str[i:])
            elif ans:
                answer.append(ans)
        
        worker([],s)
        return answer