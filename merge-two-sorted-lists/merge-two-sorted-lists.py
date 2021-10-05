# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #한 리스트가 비어있으면 다른 리스트 반환
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        
        #두개를 비교해서 작은거를 먼저 새 리스트에 넣는다-재귀
        if l2.val < l1.val :
            result = ListNode(l2.val)
            result.next = self.mergeTwoLists(l1, l2.next)
        else:
            result = ListNode(l1.val)
            result.next = self.mergeTwoLists(l1.next, l2)
        return result
        