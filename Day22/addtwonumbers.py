# link = "https://leetcode.com/explore/interview/card/microsoft/32/linked-list/170/"
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        tail = dummy
        carry=0
        while l1 or l2 or carry!=0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            summ = a+b+carry
            carry=0
            if summ>=10:
                carry = summ//10
                summ = summ%10
            tail.next=ListNode(summ,None)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            print(l2)
            print(l2)
            tail=tail.next
            
        return dummy.next