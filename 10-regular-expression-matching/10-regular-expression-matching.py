class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        text = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        
        text[0][0] = True
        
        for i in range(1, len(p)+1):
            text[i][0] = i > 1 and text[i-2][0] and p[i-1] == '*'
            
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    text[i][j] |= text[i-1][j-1]
                elif p[i-1] == '*':
                    text[i][j] |= text[i-1][j]
                    text[i][j] |= i > 1 and text[i-2][j]
                    
                    if i > 1 and p[i-2] == s[j-1] or p[i-2] == '.':
                        text[i][j] |= text[i][j-1]
        return text[-1][-1]
                    
        