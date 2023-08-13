class Solution:
    def change(self, amount: int, coins:[int]) -> int:
        res=[0]
        hasmap = {}
        def dfs(amount,pointer):
            if amount==0:
                
                return 1 
            if amount<0 or pointer==len(coins):
                return 0 
            # for x in range(pointer, len(coins)):
            #     curr.append(coins[x])
            #     dfs(amount-coins[x], curr, x)
            #     curr.pop()
            if (amount, pointer) in hasmap:
                return hasmap[(amount, pointer)] 
            hasmap[(amount,pointer)] = dfs(amount-coins[pointer], pointer) +  dfs(amount, pointer+1)
            return hasmap[(amount, pointer)]
        return dfs(amount,  pointer=0)
        