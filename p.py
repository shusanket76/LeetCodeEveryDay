def change(amount: int, coins:[int]) -> int:
        res = []
        def dfs(amount, curr, pointer):
            if amount==0:
                res.append(curr[:])
                return 
            if amount<0 or pointer>=len(coins):
                return 
            for x in range(pointer, len(coins)):
                curr.append(coins[x])
                dfs(amount-coins[x], curr, x+1)
                curr.pop()
                dfs(amount, curr, x+1)

        curr = []
        pointer = 0
        dfs(amount, curr, pointer)
        print(res)
        return len(res)
a = change(5,[1,2,5])
print(a)