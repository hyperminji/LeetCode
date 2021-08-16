# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return None
        else:
            basket = []
            node = root
            count = 0
            while basket != [] or node != None:
                if node != None:
                    basket.append(node)
                    node = node.left
                else:
                    another_node = basket.pop()
                    count = count+ 1
                    if count == k:
                        return another_node.val
                    node = another_node.right
            return None
        