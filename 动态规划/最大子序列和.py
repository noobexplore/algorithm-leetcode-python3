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
        2. 定义子问题，dp[i]为以第i个数字结尾的子序列的和
        3. 定义转移公式，dp[i] = max(0, dp[i-1]) + nums[i]
        4. 确定初始条件，dp[0] = nums[0]
        5. 确定输出结果，由于dp是对应的所有i结果，所以要取dp最大的值
        '''
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], 0) + nums[i]
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    n = [-2,1,-3,4,-1,2,1,-5,4]
    maxsum = solution.maxSubArray_dynamic(n)
    pass
