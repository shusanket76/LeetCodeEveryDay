class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        count=0
        res=""
        while n:
            res+=str(n%2)
            n=n>>1
            count+=1
        while count!=32:
            res+="0"
            count+=1
        a=0
        po=len(res)-1
        final=0
        while a<len(res):
            final+=(2**po)*int(res[a])
            a+=1
            po-=1
        return final