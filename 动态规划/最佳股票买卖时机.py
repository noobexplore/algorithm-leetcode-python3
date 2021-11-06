from typing import List


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
    
    

if __name__ == '__main__':
    n = [7,1,5,3,6,4]
    solution = Solution()
    profit = solution.maxProfit_other(n)
    pass
            
        