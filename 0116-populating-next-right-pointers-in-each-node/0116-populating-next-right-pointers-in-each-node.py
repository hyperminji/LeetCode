"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = [root]

        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1]
           
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr and curr.left:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    
        return root
        