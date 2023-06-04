# link = "https://leetcode.com/problems/3sum/"


def threeSum(nums):
    res=[]
    nums.sort()
    
    for a,b in enumerate(nums):
        
        if a>0 and b==nums[a-1]:
            continue
        l=a+1
        
        r=len(nums)-1
        
        while l<r:
            
            target = b+nums[l]+nums[r]
            print(target)
            if target==0:
                
                res.append([b,nums[l],nums[r]])
                l=l+1
                while l<r and nums[l]==nums[l-1]:
                    l=l+1
            elif target>0:
                r=r-1
            else:
                l=l+1
    return res
