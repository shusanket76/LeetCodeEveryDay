# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode()
        tail= dummy
        tail.val=1000
        tail.next = head
        fast = tail.next
        slow = tail
        while fast:
            if fast.val==slow.val:
                slow.next = slow.next.next
                fast=fast.next
            else:
                fast = fast.next
                slow = slow.next
        return dummy.next
    # ========================================================================================
    # SOLUTION 2
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        curr = head
        while curr:
            while curr.next and curr.next.val==curr.val:
                curr.next = curr.next.next
            curr=curr.next
        return head
