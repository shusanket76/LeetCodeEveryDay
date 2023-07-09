class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [[] for ab in range((amount)+1)]
        table[0]=[[]]
        for x in range(amount+1):
            if len(table[x])!=0:
                for y in coins:
                    if x+y<=amount:
                        if len(table[y+x])==0:
                            table[y+x]=table[x]+[y]
                        elif len(table[x+y])>len(table[x])+1:
                            table[x+y] = table[x]+[y]
        
        if len(table[amount])==0:
            return -1
        return len(table[amount][1:])