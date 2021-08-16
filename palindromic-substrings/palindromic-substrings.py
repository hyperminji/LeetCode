class Solution:
    def countSubstrings(self, s: str) -> int:
        pal_sub = [[i] for i in range(len(s))]
        
        for i in range(1,len(s)):
            
            curr= s[i]
            
            for start in pal_sub[i-1]:
                if start - 1>= 0 and s[start-1] == curr:
                    pal_sub[i].append(start-1)
            
            if s[i-1] == curr:
                pal_sub[i].append(i-1)
        answer = sum([len(y) for y in pal_sub])
        return answer