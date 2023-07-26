class Solution:
    def checkInclusion(self, s1: str, s2: str):
        weneed = {}
        wehave = {}
        wehaveCount=0
        weneedCount=0
        for a in s1:
            if a not in wehave:
                wehaveCount+=1

            weneed[a] = weneed.get(a,0)
            wehave[a]=wehave.get(a,0)+1
        l=0
        r=0
        while r<len(s2):
            while (r-l+1)>len(s1):
                if s2[l] in weneed:
                    weneed[s2[l]]=weneed.get(s2[l],0)-1
                    if weneed[s2[l]]+1==wehave[s2[l]]:
                        weneedCount-=1

                l+=1
            if s2[r] in weneed:
                weneed[s2[r]]=weneed.get(s2[r],0)+1
                if weneed[s2[r]]==wehave[s2[r]]:
                    weneedCount+=1
                    if weneedCount==wehaveCount:
                        return True
            r=r+1
        return False