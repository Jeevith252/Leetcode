# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        dummy= ListNode()
        cur = head
        l=[]
        while cur:
            l.append(cur.val)
            cur=cur.next
        

        l = sorted(l)
        p=dummy
        for i in l:
            p.next=ListNode(i)
            p=p.next
        
        return dummy.next