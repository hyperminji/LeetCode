class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        palindrome = lambda x : x == x[::-1]
        while i < j:
            if s[i] != s[j]:
                return palindrome(s[i:j]) or palindrome(s[i+1:j+1])
            i += 1
            j -= 1
        return True
        