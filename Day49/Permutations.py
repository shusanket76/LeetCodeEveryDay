class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums)==1:
            return [nums[:]]
        for x in range(len(nums)):
            a = nums.pop(0)
            permutation  = self.permute(nums)
        
            for perm in permutation:
                perm.append(a)
                res.append(perm)
            nums.append(a)
        return res
