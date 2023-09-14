class Solution:
    def letterCombinations(self, digits: str):
        res = []
        hasmap = {2:"abc",3:'def',4:'ghi',5:"jkl",6:"mno",7:'pqrs', 8:"tuv",9:"wxyz"}

        def dfs(pointer, curr):
            if pointer==len(digits):
                res.append(curr[:])
                return 
            
            
            for b in hasmap[int(digits[pointer])]:
                    
                    dfs(pointer+1, curr+b)
            
        pointer=0
        if len(digits)==0:
            return []
        dfs(pointer, curr="")

        return res
        