class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #그래프 만들기
        graph = collections.defaultdict(list)
        
        #그래프 순서대로 만들기
        for a,b in sorted(tickets):
            graph[a].append(b)
            
        route = []
        
        def dfs(a):
            #첫번째 값을 읽어 어휘순으로 방문
            while graph[a]:
                dfs(graph[a].pop(0)) #큐의 연산임, 맨처음 읽어들였던 값이 맨 뒤에 자리하게 되므로 마지막에 뒤집어 줘야함
            route.append(a)
            
        dfs('JFK')
        #뒤집어서 어휘 순 결과
        return route[::-1]
        
        