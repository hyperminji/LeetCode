# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: 
            return 0
        
        def dfs(root, sum):
            result = 0
            if not root: 
                return result
            if sum == root.val:
                result += 1
            result += dfs(root.left, sum-root.val)
            result += dfs(root.right, sum-root.val)
            return result
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        