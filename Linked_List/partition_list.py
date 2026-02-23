# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        dummy1 , dummy2 = ListNode() , ListNode()
        prev1 , prev2 = dummy1 , dummy2
        cur = head

        while cur:
            next_node = cur.next     
            cur.next = None  
            if cur.val < x:
                prev1.next = cur
                prev1 = prev1.next
            else:
                prev2.next = cur
                prev2 = prev2.next
            cur = next_node
        prev1.next = dummy2.next
        return dummy1.next