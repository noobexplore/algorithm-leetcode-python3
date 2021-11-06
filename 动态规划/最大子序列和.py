import sys
from typing import List


class Solution:
    def maxSubArray_greedy(self, nums: List[int]) -> int:
        max_sum, sum = -sys.maxsize, 0
        for i in range(len(nums)):
            sum += nums[i]
            max_sum = max(max_sum, sum)
            if sum < 0:
                '''核心思路，由于是连续那么但凡和小于0就从头开始算'''
                sum = 0
        return max_sum

    def maxSubArray_dynamic(self, nums: List[int]) -> int:
        '''
        动态规划，解题思路：
        1. 理解题意，首先该题解决的是连续的子序列，重点是连续，不然只找最大的相加就OK
        2. 定义子问题，dp[i]
        '''
        


if __name__ == '__main__':
    solution = Solution()
    n = [-2, -1]
    maxsum = solution.maxSubArray_greedy(n)
    pass