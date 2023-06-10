# link = "https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/187/"
class Solution(object):
    def reverseString(self,s):
            """
            :type s: List[str]
            :rtype: None Do not return anything, modify s in-place instead.
            """
            l,r=0,len(s)-1
            while l<=r:
                temp = s[l]
                s[l] = s[r]
                s[r] =temp
                l=l+1
                r=r-1