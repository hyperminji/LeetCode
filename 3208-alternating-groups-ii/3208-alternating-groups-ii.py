class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[: k - 1]
        i, j, res = 0, 1, 0
        while j < len(colors):
            if colors[j] == colors[j - 1]: i = j
            if j - i + 1 == k: 
                res += 1
                i += 1
            j += 1
        return res
        