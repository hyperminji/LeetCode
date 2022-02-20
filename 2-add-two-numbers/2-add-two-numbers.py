# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        finalnode= ListNode()
        num1=''
        num2=''
        
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
            
        result = str(int(num1[::-1]) + int(num2[::-1]))
        curr = finalnode
        for s in result[::-1]:
            curr.next = ListNode()
            curr = curr.next
            curr.val = int(s)
        
        answer = finalnode.next
        return answer