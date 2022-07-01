class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        take= 0
        
        for i in range(len(t)):
            if take < len(s):
                if s[take] == t[i]:
                    count= count +1
                    take= take+1
        if len(s)==count:
            return True
        else:
            return False