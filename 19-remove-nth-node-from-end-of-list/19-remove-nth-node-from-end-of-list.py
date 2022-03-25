# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = end = head
        
        for i in range(n):
            start = start.next
            
        if not start:
            return head.next
        
        while start.next:
            end = end.next
            start = start.next
            
        end.next = end.next.next
        return head
        