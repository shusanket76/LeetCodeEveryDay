class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l=len(s)
        r=0
        while r<=len(s)-1:
            if s[0]==" ":
                l=len(s)-r
                s.insert(l," ")
                s.remove(s[0])
                l=l-1
            else:
                s.insert(l,s[0])
                s.remove(s[0])
            r=r+1
            
        return s