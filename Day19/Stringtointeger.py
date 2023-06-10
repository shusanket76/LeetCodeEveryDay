# link = "https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/171/"

class Solution(object):
    def myAtoi(self, s):
            """
            :type s: str
            :rtype: int
            """
            l=0
            nums = 0
            sign = 1

            while  l<len(s) and  s[l]==" ":
                l=l+1
            if l<len(s) and   s[l:l+2] =="+-" or s[l:l+2]=="-+":
                return nums
            if l<len(s) and  s[l]=="+":
                l=l+1
            if l<len(s) and  s[l]=="-":
                sign=-1
                l=l+1

            while l<len(s) and s[l] in "0123456789":
                nums = str(nums)+s[l]
                l=l+1
                nums = int(nums)
            nums = sign*nums
            if nums<(-2**31):
                return (-2**31)
            if nums>((2**31)-1):
                return ((2**31)-1)
            return nums
        