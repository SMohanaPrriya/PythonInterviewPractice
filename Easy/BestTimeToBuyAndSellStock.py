"""Leet code: 121
Buy Low
Sell high

Two pointers - left - day stock is bought
right - day stock is sold
time always move forward
max(sold-bought) is the maximum profit.

"""
class Solution:
    def bestTimeToBuyAndSellStock(self, prices: list[int]) -> int:
        left, right = 0, 1 #left-buy, right-sell
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]: #profitable value
                maxProfit = max(prices[right]-prices[left], maxProfit)
            else:
                left = right #right becomes the new low
            right += 1
        return maxProfit


s = Solution()
print(s.bestTimeToBuyAndSellStock([7, 1, 5, 3, 6, 4]))