
class Solution:
    def numTrees(self, n: int) -> int:
        tree = [0] * (n+1)
        tree[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                tree[i] += tree[j] * tree[i-1-j]
        return tree[n]
        