# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        if not head:
            return head
        
        head.next = self.removeElements(head.next, val) #나머지 순회
        if head.val == val:
            head = head.next #다음 노드로 헤드노드 교체
            
        return head
        