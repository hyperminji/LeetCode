from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root,1)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right and not queue:
                return val
            if curr.right:
                queue.append((curr.right, val+1))
            if curr.left:
                queue.append((curr.left, val+1))
