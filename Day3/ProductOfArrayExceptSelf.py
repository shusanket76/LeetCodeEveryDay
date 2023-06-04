# link="https://leetcode.com/problems/product-of-array-except-self/"
# [1,2,3,4]
def productExceptSelf( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        productbeforeNumber=[]
        productafterNumber=[]
        l=0
        mulbefore = 1
        while l<=len(nums)-1:
            if l==0:
                productbeforeNumber.append(mulbefore)
            else:
                mulbefore = mulbefore*nums[l-1]
                productbeforeNumber.append(mulbefore)
            l=l+1
        r=len(nums)-1
        mulafter=1
        while r>-1:
            if r==len(nums)-1:
                productafterNumber.append(mulafter)
            else:
                mulafter = mulafter*nums[r+1]
                productafterNumber.append(mulafter)
                
            r=r-1
        for z in range(len(productbeforeNumber)):
                
                res.append(int(productafterNumber[(len(productbeforeNumber)-1)-z])*int(productbeforeNumber[z]))
            
        return res
