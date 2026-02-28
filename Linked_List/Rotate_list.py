# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        count , last = 1 ,head

        while last.next:
            last = last.next
            count+=1
        
        k = k % count
        if k == 0:
            return head

        tail = head
        last.next =head
        for i in range (count - k - 1):
            tail = tail.next
        nhead = tail.next
        tail.next = None

        return nhead