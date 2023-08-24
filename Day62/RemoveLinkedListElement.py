# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode()
        tail = dummy
        tail.next = head
        fast = tail.next
        slow = tail

        while fast:
            if fast.val==val:
                slow.next=slow.next.next
                fast = fast.next
            else:
                fast=fast.next
                slow = slow.next
        return dummy.next
