# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = ListNode(0)
        sorted_head.next = head
        sorted_tail = head
        
        curr = head.next
        
        while curr:
            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
            else:
                sorted_tail.next = curr.next
                
                insert_po = sorted_head
                while insert_po.next.val < curr.val:
                    insert_po = insert_po.next
                    
                curr.next = insert_po.next
                insert_po.next = curr
                
                curr = sorted_tail.next
        return sorted_head.next