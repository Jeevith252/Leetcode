# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        cur = head
        p , q = 0, 0

        while cur:
            if cur.val in nums:
                p+=1
            else:
                if p:
                    q+=1
                    p=0
            cur = cur.next
        if p:
            q+=1  
        return q
