class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < prev:
                buy = prices[i]
                prev = prices[i]
            elif prices[i] > prev:
                if buy == prev:
                    profit += prices[i] - prev
                    prev = prices[i]
                    buy = prices[i]

            

        return profit