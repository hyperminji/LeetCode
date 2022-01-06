# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #low이상 high이하의 값 구하기(DFS반복)
        #유효한 노드만 스택에 넣고 low~high인 경우 값을 더해나간다
        
        stack, sum = [root], 0
        
        while stack:
            node= stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum = sum + node.val
        return sum
        