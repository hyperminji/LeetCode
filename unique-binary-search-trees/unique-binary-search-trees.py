
class Solution:
    def numTrees(self, n: int) -> int:
        tree = [0] * (n+1)
        tree[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                tree[i] += tree[j] * tree[i-1-j]
        return tree[n]


#class Solution:
#    def numTrees(self, n: int) -> int:
#        
#        if n==0 or n ==1:
#            return 1
#        trees = [0]*(n+1)
#        for i in range(n):
#            left_tree = self.numTrees(i)
#            right_tree = self.numTrees(n-i-1)
#            trees = trees + left_tree*right_tree
#        return trees
#        //  Time Limit Exceeded