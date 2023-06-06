# link = "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
def findMin(nums):
        l,r=0,len(nums)-1
    
        while l<=r:
            mid = int((l+r)/2)
            if nums[l]<nums[r]:
                return nums[l]
            if nums[l]<nums[mid]:
                if l==mid:
                    l=mid+1
                else:
                    l=mid
            else:
                if r==mid:
                    r=mid-1
                else:
                    r=mid
        a=l+1
        if a>len(nums)-1:
            return nums[0]
        return nums[a]
