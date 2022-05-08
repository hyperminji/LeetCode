class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #토폴로지
        #0 방문전, 1 방문, -1 방문 후
        graph = [set() for _ in range(numCourses)]
        
        for des, start in prerequisites:
            graph[start].add(des)
        visit, order = [0]*numCourses, []
        
        def dfs(x):
            visit[x] = -1
            for y in graph[x]:
                if visit[y] < 0 or (not visit[y] and dfs(y)):
                    return True
            visit[x] = 1
            order.append(x)
            return False
        
        for x in range(numCourses):
            if not visit[x] and dfs(x):
                return []
        return order[::-1]
        
        