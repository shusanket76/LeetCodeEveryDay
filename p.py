def characterReplacement(s: str, k: int):
        hasmap = {}
        l=r=0
        res= 0
        while r<len(s):
            hasmap[s[r]]=hasmap.get(s[r], 0)+1
            while (r-l+1)-max(hasmap.values())>k:
                hasmap[s[l]] = hasmap.get(s[l],0)-1
                l+=1
            else:
                res = max(res, r-l+1)
                r+=1
        return res
        
a = characterReplacement("AABABBA", 1)   
print(a)