class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bear = prices[0]
        profit = 0

        for i in prices:
            bear = min(bear, i)
            profit = max(profit, abs(i - bear))
        
        return profit
        
        '''bear = prices[0]
        profit = 0

        for i in range(len(prices)):
            bear = min(prices[i], bear)
            if bear == prices[i]:
                bull = bear
                for j in range(i+1,len(prices)):
                    bull = max(prices[j], bull)
                    if bull == prices[j]:
                        profit = max(profit, bull - bear)
        
        return profit'''