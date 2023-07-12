class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table=[[0 for x in range((n)+1)] for y in range((m)+1)]
        table[1][1]=1
        ab=0
        
        while ab<(m+1):
            cd=0
            while cd<(n+1):
                print(ab,cd)
                if table[ab][cd]!=0:
                    if cd+1<n+1:
                        table[ab][cd+1]+=table[ab][cd]
                    if ab+1<m+1:
                        table[ab+1][cd]+=table[ab][cd]
                cd=cd+1
            ab=ab+1
        
        return table[m][n]
