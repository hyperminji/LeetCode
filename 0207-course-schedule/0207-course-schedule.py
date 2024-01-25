class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #그래프 선언
        graph = collections.defaultdict(list)
        
        #그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set() #방문한 노드 저장
        
        def dfs(i):
            #순환구조면 false
            if i in traced:
                return False
                 
            #이미 방문한 노드면 True
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
                
            #탐색 후 순환노드 삭제->자식노드에 가서 헷갈릴 수 있음
            traced.remove(i)
            #탐색 후 방문노트 추가 
            visited.add(i)
            
            return True
        
        
            #순환구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
        