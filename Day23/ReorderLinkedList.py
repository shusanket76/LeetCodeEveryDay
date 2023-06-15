# link = 'https://leetcode.com/problems/reorder-list/description/'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s,f=head,head.next

        while f and f.next:
            s=s.next
            f=f.next.next
        second = s.next
        s.next=None
        prev1,curr1=None, second
        while curr1:
            nxr = curr1.next
            curr1.next=prev1
            prev1=curr1
            curr1=nxr
 
       

        while prev1:
            tmp1,tmp2=head.next, prev1.next
            head.next= prev1
            prev1.next=tmp1
            head=tmp1
            prev1=tmp2
        




  

      

            
