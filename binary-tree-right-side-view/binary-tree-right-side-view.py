# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
# collect right value,  save it
        result = []
        if root:
            stack = [root]
        else:
            return []
    
        while stack:
            newstack = []
            result.append(stack[-1].val)
            for n in stack:
                if n.left :
                    newstack.append(n.left)
                if n.right:
                    newstack.append(n.right)
                stack = newstack
        return result
