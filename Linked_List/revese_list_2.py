# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for i in range(left-1):
            prev = prev.next
        
        cur = prev.next

        for i in range(right - left):
            p = cur.next
            cur.next=p.next
            p.next=prev.next
            prev.next=p
        return dummy.next