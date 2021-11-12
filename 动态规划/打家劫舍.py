"""
题目描述：
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""

from typing import List


class Solution:
    def rob_induction(self, nums: List[int]) -> int:
        """
        动态规划1：
        1. 理解题意：
            - 不能连续进行累加计算
        2. 确定状态：
            - dp[i] 为第i家所累计的金额
        3. 转移方程：
            - dp[i] = max(dp[:i-1]) + nums[i]
            - 以上转移方程的解释：
                - d[:i-1]表示除了相邻的人家剩余的人家中最大的金额累计
        4. 边界条件：
            - 需要从第0家和第1家进行计算
            - dp[0] = nums[0]
            - dp[1] = nums[1]
        5. 返回的值：
            - 由于该过程dp求的是通过每家的最大金额，所以最后返回也要max(dp)
        6. 优化的点：
            - 缺点还是有很多的重复计算
            - 思考能否减少重复计算点
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[:i-1]) + nums[i]
        return max(dp)
    
    def rob_dynamic(self, nums: List[int]) -> int:
        """
        动态规划2：
            - 思路一样，区别在于定义状态的时候这里用一个二维数组去进行存储之前的最大值
        2. 确定状态：
            - dp[i][0] 表示第i家没有被偷的最大累计金额；
            - dp[i][1] 表示第i家被偷了累计最大金额；
        3. 状态转移方程：
            - dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            - 以上的解释是该家没有被偷，那么之前累计金额就不管前面偷没偷过了
            - dp[i][1] = dp[i-1][0] + nums[i]
            - 如果该家被偷了，那么只能取前面没被偷的金额加上该家的金额
        4. 边界条件：
            - dp[0][0] = 0
            - dp[0][1] = nums[i]
        5. 返回结果：
            - 最终的结果还是跟上面的一样，由于是求得从每家出发的最大金额所以最后得返回
            - max(dp[len(nums)-1][0], dp[len(nums)-1][1])
        6. 优化的点：
            - 二维数组还是有点浪费空间
        """
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])


if __name__ == '__main__':
    n = [2,7,9,3,1]
    solution = Solution()
    rob = solution.rob_dynamic(n)
    pass
        