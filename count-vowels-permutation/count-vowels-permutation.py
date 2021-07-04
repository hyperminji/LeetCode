#dp bottom-up time:O(n), space:O(1)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        mod = 10 ** 9 + 7
        for _ in range(2, n + 1):
            a, e, i, o, u = (e + u + i) % mod, (a + i) % mod, (e + o) % mod, i, (o + i) % mod 
        return sum([a, e, i, o, u]) % mod  
        