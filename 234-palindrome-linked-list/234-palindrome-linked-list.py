# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #반 자른다 -> 뒤집는다 -> 비교해서 같으면 회문 아니면 노회문
        fast = slow = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
        fast = head
        slow = self.reverse(slow)
        
        while slow != None:
            if slow.val != fast.val:
                return False
            
            fast = fast.next
            slow = slow.next
        return True
    
    
   
    def reverse(self, head: ListNode)-> ListNode:
        pre_nd = None
        
        while head:
            next_nd = head.next
            head.next = pre_nd
            pre_nd = head
            head = next_nd
        return pre_nd