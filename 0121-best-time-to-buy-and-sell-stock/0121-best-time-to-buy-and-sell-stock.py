class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        n, max_prices, max_price = len(prices), prices.copy(), 0
        
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i+1])
            max_prices[i] = max_price
        # print(max_prices)
        
        for i in range(n-1):
            answer = max(answer, max_prices[i]-prices[i])
        
        return max(answer, 0)