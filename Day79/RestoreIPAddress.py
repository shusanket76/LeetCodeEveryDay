class Solution:
    def restoreIpAddresses(self, s):

        res = []

        if len(s)>12:
            return res

        def dfs(i,dots,currIp):
            if i==len(s) and dots==4:
                res.append(currIp[:-1])
                return
            if dots>4:
                return
            for j in range(i,min(i+3, len(s))):
                if int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                    dfs(j+1, dots+1, currIp+s[i:j+1]+".")
            

        i=0
        dots=0
        currIp=""
        dfs(i, dots, currIp)
        return res