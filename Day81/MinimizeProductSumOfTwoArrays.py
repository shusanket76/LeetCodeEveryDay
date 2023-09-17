class Solution:
    def minProductSum(self, nums1, nums2) -> int:
        nums2c = nums2.copy()
        nums2c.sort()
        hasmap = {}
        for x in range(len(nums2c)):
            if nums2c[x] not in hasmap:
                hasmap[nums2c[x]] = [x]
            else:
                hasmap[nums2c[x]].append(x)
        nums1.sort()
        res = 0
        for y in nums2:
            a = hasmap[y]
            if len(a)==1:
                res+=y*nums1[len(nums1)-1-a[0]]
            else:
                res+=y*nums1[len(nums1)-1-a[0]]
                a.pop(0)

        return res