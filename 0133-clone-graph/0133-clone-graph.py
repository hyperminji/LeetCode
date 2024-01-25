"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodecy = Node(node.val, [])
        dic = {node:nodecy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in dic:
                    neicopy = Node(nei.val, [])
                    dic[nei] = neicopy
                    dic[node].neighbors.append(neicopy)
                    queue.append(nei)
                else:
                    dic[node].neighbors.append(dic[nei])
        return nodecy
        