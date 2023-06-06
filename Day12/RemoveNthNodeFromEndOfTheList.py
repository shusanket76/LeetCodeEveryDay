# link = "https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/"
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy  = ListNode(0,head)
        s,f=dummy,head
        while n>0:
            f=f.next
            n=n-1
        
        while f:
            s=s.next
            f=f.next
        
        s.next=s.next.next
        return dummy.next
# SOLUTIN 2 HINT = YOU CAN FIRST COUNT THE ELEMENTS IN THE LINKED LIST 
# AND SUBTRACT THE n NUMBER FROM THE TOTAL COUNT AND REMOVE THAT NODE FROM THE LINKED LIST