import collections
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n2nxt = collections.defaultdict(set)
        lenbom = len(bombs)
        
        for i in range(lenbom):
            xi,yi,ri = bombs[i]
            
            for j in range(lenbom):
                if i ==j:
                    continue
                    
                xj, yj, rj = bombs[j]
                
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2: 
                    n2nxt[i].add(j)
        
        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            for nxt in n2nxt[n]:
                dfs(nxt)

        answer = 0
        for i in range(lenbom):
            seen = set()
            dfs(i)
            answer = max(answer, len(seen))
        return answer