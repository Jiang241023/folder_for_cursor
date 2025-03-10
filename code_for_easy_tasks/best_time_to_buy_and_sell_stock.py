from typing import List

class Solution:
    # 类内部的方法必须统一缩进（此处用4个空格）
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
    
    # 确保 minProfit 方法与 maxProfit 对齐（同属于 Solution 类）
    def minProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_price = prices[0]
        min_profit = float('inf')  # 修正逻辑错误：初始化应为极大值
        for price in prices[1:]:
            if price > max_price:
                max_price = price
            else:
                profit = max_price - price
                if profit < min_profit:
                    min_profit = profit
        return min_profit if min_profit != float('inf') else 0

profit = Solution()
prices = [7,1,5,3,6,4,9]
print(f"Max profit: {profit.maxProfit(prices)}")  # 输出 5
print(f"Min profit: {profit.minProfit(prices)}")

