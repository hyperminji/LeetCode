#재귀로 높이차이 계산

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            #단차 유:-1, 이외: 높이따라 1증가
            if left == -1 or right == -1 or abs(left-right)>1:
                return -1
            return max(left, right)+1
        
        return check(root) != -1
        