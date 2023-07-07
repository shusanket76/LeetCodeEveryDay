class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table= [0 for x in range(n+1)]
        table[0]=1
        a = 0
        while a<=n:
            if a+1<=n:
                table[a+1]+=table[a]
            if a+2<=n:
                table[a+2]+=table[a]
            a=a+1
        return table[n]