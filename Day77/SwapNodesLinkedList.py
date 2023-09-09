# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k: int):
        first, second, third = head, head, head
        a = 1
        while first:
            if a==k:
                break
            first=first.next
            second = second.next
            a+=1
        while second.next:
            second = second.next
            third = third.next
        temp = first.val
        first.val = third.val
        third.val = temp
        return head