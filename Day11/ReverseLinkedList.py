# link = "https://leetcode.com/problems/reverse-linked-list/"

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev,curr=None,head
        while curr:
            nxt = curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev