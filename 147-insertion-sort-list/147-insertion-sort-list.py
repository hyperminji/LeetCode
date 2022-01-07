# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #초깃값 변경
        cur = parent = ListNode(0) #None이면 에러발생
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            #필요한 경우에만 cur포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur=parent
        return parent.next
        