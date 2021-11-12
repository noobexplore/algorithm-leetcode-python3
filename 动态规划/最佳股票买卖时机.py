from typing import List

'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        蛮力法, 要超时
        '''
        maxprofit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    if prices[j] - prices[i] > maxprofit:
                        maxprofit = prices[j] - prices[i]
        return maxprofit
    
    def maxProfit_other(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)-1):
            post = max(prices[i+1:len(prices)])
            if post - prices[i] > maxprofit:
                maxprofit = post - prices[i]
        return maxprofit

    def maxProfit_dynamic(self, prices: List[int]) -> int:
        '''
        动态规划：
        1. 理解题意：
            - 首先只能进行一次的买和卖
            - 注意买要在卖前面
        2. 确定子状态：
            - dp[i][0]: 第i天手里没有股票的最大利润；
            - dp[i][1]: 第i天手里有股票的最大利润；
        3. 状态转移方程：
            - dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            - 表示第i天手里没有股票的时候，分以下两种情况：
                - 前一天也没有股票，就以前一天利润为准；
                - 今天要卖，那么就要根据前一天持有股票的利润加上当天的股票价格；
            - dp[i][1] = max(dp[i-1][1], -prices[i])
                - 前一天手里就有股票，以前一天有股票利润为准；
                - 今天刚好买，所以利润就只能是以今天的股票价格为准；
        4. 初始状态：
            - dp[0][0] = 0 第一天没有买股票；
            - dp[0][1] = -prices[0] 第一天买了股票；
        5. 返回值：
            - 这里只能是看没有股票的情况中利润最大的值
            - max(dp[-1][0])
        6. 优化的点：
            - 只用一个数组去记录最近的值
        '''
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[-1][0]

    def maxProfit_dynamic2(self, prices: List[int]) -> int:
        # 只用两个变量去保存最终的值
        nohold = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            temp1 = max(nohold, hold+prices[i])
            temp2 = max(hold, -prices[i])
            nohold = temp1
            hold = temp2
        return nohold
    

if __name__ == '__main__':
    n = [7,1,5,3,6,4]
    solution = Solution()
    profit = solution.maxProfit_dynamic2(n)
    pass
            
        