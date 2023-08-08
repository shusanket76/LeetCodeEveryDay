class Solution:
    def subsets(self, nums: [int]) ->[[int]]:
        res = [[]]
        def dfs(nums, pointer,curr):

            # =======================================================

            #     if pointer>len(nums)-1:
            #     if curr not in res:
            #         res.append(curr[:])
            #     return 

    
            
            # curr.append(nums[pointer])
            
            # dfs(curr,pointer+1)
            # curr.pop()
            # dfs(curr,pointer+1)
            # ===============================================
            if  pointer>len(nums)-1:
                return curr
            curr.append(nums[pointer])
            newcurr = curr[:]
            res.append(newcurr)
            dfs(nums, pointer+1, curr)
            curr.pop()
            dfs(nums,pointer+1, curr)
            

            
            
        pointer = 0
        dfs(nums, pointer, [])
        return res