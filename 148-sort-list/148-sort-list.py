#O(n logn), wjdfufdkfrhflwma rngus 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head # p 는 포인터
        l = []
        while p:
            l.append(p.val)
            p = p.next
            
        #정렬
        l.sort()
        
        #리스트-> 연결리스트
        p = head
        for i in range(len(l)):
            p.val = l[i]
            p = p.next
        return head