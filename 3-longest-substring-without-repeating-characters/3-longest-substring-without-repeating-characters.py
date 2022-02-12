class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        answer = 0
        t = ''
        while  i < len(s):
            
            if s[i] not in t:
                t = t+s[i]
                answer = max(answer, len(t))
            else:
                index = t.index(s[i])
                t=t[index+1:]+s[i]
            i= i+1
        return answer
        