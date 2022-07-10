class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(char_index, i, j):
            if self.found: 
                return        
            if char_index == k:
                self.found = True              
                return 

            if i < 0 or i >= m or j < 0 or j >= n: 
                return 
            temp = board[i][j]
            if temp != word[char_index]: 
                return

            board[i][j] = "#"
            dfs(char_index+1, i+1, j)
            dfs(char_index+1, i-1, j)
            dfs(char_index+1, i, j+1)
            dfs(char_index+1, i, j-1)
            board[i][j] = temp

            
        self.found = False
        m = len(board)
        n = len(board[0])
        k = len(word)
        
        for i, j in product(range(m), range(n)):
            if self.found:
                return True          
            dfs(0, i, j)
        return self.found
        