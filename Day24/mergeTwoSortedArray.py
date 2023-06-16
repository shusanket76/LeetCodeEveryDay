# link ="https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/258/"

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a= m
        b=0
        while a<len(nums1):
            nums1[a]=nums2[b]
            a=a+1
            b=b+1

        for x in range(1,len(nums1)):
            anchor = nums1[x]
            j=x-1
            while j>=0 and  nums1[j]>anchor:
                nums1[j+1]=nums1[j]
                j=j-1
            nums1[j+1] = anchor
        