# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #empty list
        if root == None:
            return []
        
        current = [root]
        answer = []
        
        
        while current != []:
            value = []
            nextval = []
            
            for node in current:
                value.append(node.val)
                if node.left :
                    nextval.append(node.left)
                if node.right:
                    nextval.append(node.right)
            answer.append(value)
            current = nextval
            
            
        return answer