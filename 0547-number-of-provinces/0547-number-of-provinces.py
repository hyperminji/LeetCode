class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited= set()
        
        def dfs(cityi):
            cityicon = isConnected[cityi]
            visited.add(cityi)
            
            for cityj in range(n):
                if (cityj not in visited) and (cityicon[cityj] == 1) and (cityi != cityj):
                    dfs(cityj)
            return
        numProvinces = 0
        for cityi in range(n):
            if cityi not in visited:
                dfs(cityi)
                numProvinces += 1
        return numProvinces
        