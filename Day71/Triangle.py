class Solution:
    def minimumTotal(self, triangle) -> int:
        res = [float("inf")]
        hasmap = {}
        def dfs(ap, sp, currsum):
            if (ap,sp) in hasmap:
                return hasmap[(ap,sp)]+currsum
            if ap==len(triangle):
                return currsum
            
            a1 = dfs(ap+1, sp, currsum+triangle[ap][sp])
            
            a2 = dfs(ap+1, sp+1, currsum+triangle[ap][sp+1])
            res[0] = min(a1, a2)
            hasmap[(ap,sp)] = res[0]-currsum
        
            return res[0]

        araypointer = 0
        singlepointer = 0
    
        currsum = triangle[0][0]
        dfs(araypointer+1, singlepointer, currsum)
        if res[0] == float('inf'):
            return currsum
        return res[0]