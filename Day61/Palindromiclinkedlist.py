from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        stack = deque()
        first = head
        prev = None
        while first:
            stack.append(first.val)
            nxt = first.next
            first.next = prev
            prev = first
            first = nxt
        while prev:
            if stack.popleft()!=prev.val:
                return False
            prev = prev.next
        return len(stack)==0
