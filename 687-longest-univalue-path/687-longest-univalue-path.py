# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node:TreeNode):
            
            if node is None:
                return 0
            
            #존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            #현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val ==node.val:
                left = left+1
            else:
                left = 0
                
            if node.right and node.right.val ==node.val:
                right = right+1
            else:
                right = 0
                
            #왼쪽과 오른쪽 자식 노드 간 거리의 최대값이 결과임
            self.result = max(self.result, left+right)
            #자식노드 중 큰값
            return max(left, right)
        
    
        dfs(root)
        return self.result
                
        
        