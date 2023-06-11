# link = "https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/166/"


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def recursion(arr):
            if len(arr)==1:
                return arr[0]
            return recursion(arr[1:len(arr)])+ " "+arr[0]
        lent = len(s)
        l=0
        word=""
        arr=[]
        while l<lent:
            if l<lent and s[l]==" ":
                if len(word)!=0:
                    arr.append(word)
                    word=""

                l=l+1
            elif l<lent and s[l]!=" ":
                word = word+s[l]
                l=l+1
        if word not in " ":
            arr.append(word)
        ans = recursion(arr)


        return ans

