# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #root가 아니면
        if not root:
            return
        
        queue = deque([root.right, root.left])
        while queue:
            node = queue.pop()
            if not node:
                continue
            root.right = node
            root.left = None
            root = root.right
            queue.append(node.right)
            queue.append(node.left)
            
        
        