def partition(s: str):
        res = []
        part = []

        def dfs(i):
            if i>=len(s):
                res.append(part[:])
                return  
            for a in range(i,len(s)):
                if pali(s,i,a):
                    part.append(s[i:a+1])
                    dfs(a+1)
                    part.pop()
        def pali(stri,l,r):
            while l<r:
                if stri[l]!=stri[r]:
                    return False
                l+=1
                r-=1
            return True

        dfs(0)
        return res

a = partition("abcecab")
print(a)
