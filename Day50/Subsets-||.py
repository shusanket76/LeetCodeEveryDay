class Solution:
    def subsetsWithDup(self, nums:[int]):
        res = [[]]
        def dfs(nums,pointer,curr):
            if pointer>len(nums)-1:
                return nums
            curr.append(nums[pointer])
            newcurr=curr[:]
            if sorted(newcurr) not in res:
                res.append(sorted(newcurr))
            dfs(nums,pointer+1, curr)
            curr.pop()
            dfs(nums,pointer+1,curr)




        pointer = 0
        curr=[]
        dfs(nums, pointer, curr)
        return res
        