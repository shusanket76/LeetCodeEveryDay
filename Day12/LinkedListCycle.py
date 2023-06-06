# link = "https://leetcode.com/problems/linked-list-cycle/submissions/965248445/"

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hasmap={}
        s,f=head,head
        while f and f.next:

            if f in hasmap:
                return True
            else:
                hasmap[s] = True
            s=s.next
            f=f.next.next
        return False
    # ==============================================================SOLUTION2======================================
    
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
      
        s,f=head,head
        while f and f.next:
            s=s.next
            f=f.next.next

            if f==s:
                return True
     
 
        return False