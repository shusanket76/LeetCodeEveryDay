# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        n = int((1+n)/2)
        while guess(n)!=0:
            if guess(n)<0:
                end = n-1
            elif guess(n)>0:
                start = n+1
            n = int((start+end)/2)
        return n
        