class Solution:
    def combinationSum2(self, candidates, target: int):

        res = []
        candidates = sorted(candidates)
        def dfs(total,pos,curr):
            if total==target:
                newcurr = curr[:]
              
                res.append(newcurr)
                return
            if len(candidates)==0 or total>target:
                return
            prev=-1
            for x in range(pos,len(candidates)):
                if candidates[x]==prev:
                    continue
                curr.append(candidates[x])
                dfs(total+candidates[x],x+1,curr)
                curr.pop()
                prev=candidates[x]
        total=0
        curr=[]
        dfs(total,0,curr)
        return res

        