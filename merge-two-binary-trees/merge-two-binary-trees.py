# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#재귀
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            result  = TreeNode(root1.val + root2.val)
            result.right = self.mergeTrees(root1.right, root2.right)
            result.left = self.mergeTrees(root1.left, root2.left)
            
            return result
        else:
            return root1 or root2 #값이 있는 노드만 
            
        