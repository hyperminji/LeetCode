# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            #전위 순회 결과 -> 중위 순회의 분할 인덱스임
        if inorder:
            index = inorder.index(preorder.pop(0))
                
            #중위 순회 결과를 분할 정복-> 이진트리 복구
            tnode = TreeNode(inorder[index])
            tnode.left = self.buildTree(preorder, inorder[0: index])
            tnode.right = self.buildTree(preorder, inorder[index+1: ])
        
            return tnode