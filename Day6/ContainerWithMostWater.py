# link = https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        l,r=0,len(height)-1
        while l<r :
            h = min(height[l],height[r])
            b=r-l
            res = max(res,h*b)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return res 
a = maxArea([1,8,6,2,5,4,8,3,7])
print(a)