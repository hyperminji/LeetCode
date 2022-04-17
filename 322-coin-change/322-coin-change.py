class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #You may assume that you have an infinite number of each kind of coin.
        
        if amount == 0:
            return 0
        
        queue = [[0,0]]
        visited = {0}
        lev = 0
        for node, lev in queue:
            for coin in coins:
                if node + coin in visited:
                    continue
                if node + coin == amount:
                    return lev+1
                elif node + coin < amount:
                    queue.append([node+coin, lev+1])
                    visited.add(node+coin)
                
                
        return -1
        
        