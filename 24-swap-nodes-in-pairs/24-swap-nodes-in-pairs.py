# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(0)
        prev.next = head
        
        while prev.next and prev.next.next:
            x = prev.next
            y = prev.next.next
            z = prev.next.next.next
            prev.next = y
            prev.next.next = x
            prev.next.next.next = z
            prev = prev.next.next
        return dummy.next
        