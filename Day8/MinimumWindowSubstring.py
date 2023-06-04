# link = "https://leetcode.com/problems/minimum-window-substring/"


def minWindow(s, t):
        weNeed = 0
        weHave = 0
        weNeedHasmap={}
        weHaveHasmap={}
        for x in t:
            if x in weHaveHasmap:
                weNeedHasmap[x] = weNeedHasmap.get(x,0)+1
            else:
                weNeedHasmap[x] = weNeedHasmap.get(x,0)+1
                weHaveHasmap[x] = weHaveHasmap.get(x,0)+0
                weNeed=weNeed+1
        l=0
        r=0
        res=["","",float("inf")]
        while r<len(s):
            if s[r] in weHaveHasmap:
                weHaveHasmap[s[r]] = weHaveHasmap[s[r]]+1
                if weHaveHasmap[s[r]]==weNeedHasmap[s[r]]:
                    weHave+=1
            while weHave==weNeed:
                if res[2]>r-l:
                    res=[l,r,r-l]
                if s[l] in weHaveHasmap:
                    weHaveHasmap[s[l]] = weHaveHasmap.get(s[l],0)-1
                    if weHaveHasmap[s[l]]<weNeedHasmap[s[l]]:
                        weHave=weHave-1
                l=l+1
            r=r+1
        if res[0]=="":
            return ""
        return s[int(res[0]):int(res[1]+1)]