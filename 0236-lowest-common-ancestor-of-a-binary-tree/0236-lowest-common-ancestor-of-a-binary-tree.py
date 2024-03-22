# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        stack = [root]

        # 부모
        parent = {root: None}

        # p,q찾을때 까지 반복
        while p not in parent or q not in parent:

            node = stack.pop()

            # 부모를 계속 저장한다
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        #q 조상
        grandparents = set()

        
        while p:
            grandparents.add(p)
            p = parent[p]

        # q 첫번째 조상
        
        while q not in grandparents:
            q = parent[q]
        return q
        