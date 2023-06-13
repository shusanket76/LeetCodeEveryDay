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
        tailnode= dummy
        prev1,curr1=None,l1
        while curr1:
            nxt = curr1.next
            curr1.next=prev1
            prev1=curr1
            curr1=nxt
        prev2,curr2 = None,l2
        while curr2:
            nxt1 = curr2.next
            curr2.next=prev2
            prev2=curr2
            curr2=nxt1
        add=0
        while prev1 or prev2 or add:
            val1=prev1.val if prev1 else 0
            val2=prev2.val if prev2 else 0
            
            sumans = val1+val2+add
            add=0
            if sumans>=10:
                temp = sumans%10
                add = sumans//10
                sumans=temp
            tailnode.next=ListNode(sumans)
            tailnode.next.val=sumans
            prev1=prev1.next if prev1 else None
            prev2=prev2.next if prev2 else None

            tailnode=tailnode.next
   
        prev3,curr3=None,dummy.next
        while curr3:
            nxt3 = curr3.next
            curr3.next=prev3
            prev3=curr3
            curr3=nxt3
        return prev3
     