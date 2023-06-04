# link="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=l+1
        profit =0
        while r<=len(prices)-1:
            if prices[l]>prices[r]:
                l=l+1
                r=l+1
            else:
                profit = max(profit, prices[r]-prices[l])
                r=r+1
        return profit
            
            