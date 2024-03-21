class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxNum = 0

        while r < len(prices):

            sumNum = prices[r] - prices[l]
            if sumNum > 0:
                maxNum = max(sumNum,maxNum)
            else:
                l = r
            r+=1

        return maxNum