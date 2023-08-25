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
    # =======================================================================
    # SOLUTION 2
    # class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     res =[]
    #     nums.sort()
    #     def dfs(pointer, curr):
    #         if pointer == len(nums):
    #             res.append(curr[:])
    #             return 
    #         curr.append(nums[pointer])
    #         dfs(pointer+1, curr)
    #         curr.pop()
    #         while pointer+1<len(nums) and nums[pointer]==nums[pointer+1]:
    #             pointer+=1
    #         dfs(pointer+1,curr)
    #     dfs(0, curr=[])
    #     return res
        