class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        lowest = 100001
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            if prices[i]-lowest> diff:
                diff = prices[i]-lowest
                    
        return diff