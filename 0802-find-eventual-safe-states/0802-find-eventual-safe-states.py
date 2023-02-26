class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def check_cycle(node,graph,vis):
            if vis[node]==2:
                return True
            vis[node]=2
            for nei in graph[node]:
                if vis[nei]!=1:
                    if check_cycle(nei,graph,vis):
                        return True
            vis[node]=1
            return False
                
        n=len(graph)
        vis=[0]*(n)
        for i in range(n):
            if vis[i]==0:
                if check_cycle(i,graph,vis):
                    continue
        answer=[]
        for i in range(n):
            if vis[i]==1:
                answer.append(i)
        return answer
        