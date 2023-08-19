class Solution:
    def trap(self, height:[int]) -> int:
        maxleft = [0 for x in range(len(height))]
        maxright = [0 for x in range(len(height))]
        mal = 0
        for x in range(len(height)):
            mal = max(mal, height[x])
            maxleft[x] = mal
        mar = 0 
        for y in range(len(height)-1,-1,-1):
            mar = max(mar, height[y])
            maxright[y] = mar

        res = 0
        for z in range(len(height)):
            a = min(maxleft[z], maxright[z])
            b = a-height[z]
            if b>0:
                res+=b
        return res
