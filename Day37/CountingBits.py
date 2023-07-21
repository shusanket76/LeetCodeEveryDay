class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        hasmap={}
        for x in range(n+1):
            # print(x)
            binx = int(x)
            # print(binx)
            temp=0
            while binx!=0:
                if binx not in hasmap:
                    temp+=binx%2
                    print(temp,binx)
                    binx=int(binx/2)
                else:
                    temp+=hasmap[binx]
                    binx=0
            hasmap[x]=temp
            res.append(temp)
        return res
