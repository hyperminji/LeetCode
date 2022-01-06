#BST의 우측 자식 노드는 항상 부모 노드보다 큰 값이다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        #중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val = self.val+ root.val
            root.val = self.val
            self.bstToGst(root.left)
            
        return root
        