# link="https://leetcode.com/problems/search-in-rotated-sorted-array/"

def search( nums, target):
    l,r=0,len(nums)-1
    while l<=r:
        mid = int((l+r)/2)
        if nums[mid]==target:
            return mid
        if nums[l]<=nums[mid]:
            if target>nums[mid] or target<nums[l]:
                l=mid+1
            else:
                r=mid-1
        else:
            if target<nums[mid] or target>nums[r]:
                r=mid-1
            else:
                l=mid+1

                       
    return -1
            
                

a  = search([4,5,6,7,1,2,3],6)
print(a)
