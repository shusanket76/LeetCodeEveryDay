# link = "https://leetcode.com/problems/merge-k-sorted-lists/submissions/"
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLl(l1,l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next = l1
                    l1=l1.next
                    tail=tail.next
                else:
                    tail.next = l2
                    l2=l2.next
                    tail=tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        l,r=0,1
        first =True
        a = ListNode("")
        if len(lists)==1:
            return lists[0]
        if len(lists)==0:
            return a
        while r<len(lists):
            if first:
                a = mergeTwoLl(lists[l], lists[r])
                first = False
                r=r+1
            else:
                a = mergeTwoLl(a, lists[r])
                r=r+1
        return a

            

