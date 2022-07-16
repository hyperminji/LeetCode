# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        last = head
        lenth = 1
        
        while last.next:
            last = last.next
            lenth+=1
            
        k = k % lenth
        
        last.next = head
        
        temp = head
        for _ in range( lenth - k - 1):
            temp = temp.next
            
        result = temp.next
        temp.next = None
        
        return result