class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        hasmap={}
        def climb(i):
            if i in hasmap:
                return hasmap[i]
            if i <= 1:
                return cost[i]
            
            hasmap[i] =  cost[i] + min(climb(i-1), climb(i-2))
            return hasmap[i]
        n = len(cost)
        return min(climb(n-1), climb(n-2))