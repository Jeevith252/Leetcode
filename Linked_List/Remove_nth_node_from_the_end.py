# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return None

        cur = head
        prev=None

        while cur :
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        
        count = 1
        dummy =  ListNode()
        prev2 =dummy
        cur =prev

        while cur and count<=n:
            if count ==  n:
                prev2.next = cur.next
                break
            else:
                prev2.next =cur
                prev2 = prev2.next
                cur = cur.next
                count+=1
        cur = dummy.next
        prev =  None

        while cur :
            t= cur.next
            cur.next = prev
            prev = cur
            cur =t
        return prev



