# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        prev = dummy
        cur = head

        while cur and cur.next:
            prev.next = cur.next 
            cur.next = cur.next.next
            prev.next.next=cur

            prev =cur
            cur = cur.next
        return dummy.next

  
  