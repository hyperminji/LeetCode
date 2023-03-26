class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        m = defaultdict(int)
        result = []
        
        mapcode = { 'A':0, 'C':1, 'G':2, 'T':3 }
        
        base = 4
        hsh = 0
        
        for i in range(10):
            current = mapcode[s[i]]
            hsh*= base
            hsh += current
        
        m[hsh]=1
        
        l = 1
        while l+9 < len(s):
            left = mapcode[s[l-1]]
            right = mapcode[s[l+9]]
            
            hsh -=left*base**9
            hsh *=base
            hsh +=right
            
            m[hsh] +=1
            
            if m[hsh] == 2:
                result.append(s[l:l+10])

            l +=1
        return result
            