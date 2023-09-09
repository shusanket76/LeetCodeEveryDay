# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        fast=head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev= None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        res = 0
        while prev:
            res = max(res, head.val+prev.val)
            prev = prev.next
            head=head.next
        return res
