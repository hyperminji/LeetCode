# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, answer, floor = float('-inf'), 0, 0

        q = collections.deque()
        q.append(root)

        while q:
            floor += 1
            curr_floor = 0
            # Iterate over all the nodes in the current level.
            for _ in range(len(q)):
                node = q.popleft()
                curr_floor += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < curr_floor:
                max_sum, answer = curr_floor, floor
           
        return answer
        
        