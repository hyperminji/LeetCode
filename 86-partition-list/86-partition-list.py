
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        front = front_head = ListNode(0)
        back = back_head = ListNode(0)
        
        while head:
            if head.val < x:
                front.next = head
                front = front.next
                
            else:
                back.next = head
                back= back.next
            
            head = head.next
            
        back.next = None
        front.next = back_head.next
        return front_head.next
                
        
        