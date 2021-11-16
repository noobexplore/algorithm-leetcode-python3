class Solution:
    def longestCommonSubsequence_dynamic_planning(self, text1: str, text2: str) -> int:
        """
        动态规划：
        1. 理解题意：
            - 最长的序列（有顺序）
        2. 定义子状态：
            - dp[i][j] 以text1中第i个字符和text2中第j个字符结尾的子序列的长度；
        3. 状态转移方程：
            - if ch[i] == ch[j]: dp[i][j] = dp[i-1][j-1] + 1
            - else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        4. 初始化和边界条件：
            - dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
            - 要注意的是多出一行一列全部为0，方便后续计算
        5. 返回值：
            - 由于是一直递进计算的，所以最终返回dp[-1][-1]就为最大序列长度
        6. 优化的点：
            - 有些值重复保存了
        """
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text2[j-1] == text1[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

    def longestCommonSubsequence_dynamic_planning1(self, text1: str, text2: str) -> int:
        """
        改进版本：
            - 用一个temp保存dp[i][j-1]的值
            - 用一个一维数组来进行保存
            - 每次就比较temp和dp[i-1]
            - 返回的值就为dp[-1]
        """
        dp = [0 for _ in range(len(text1)+1)]
        for i in range(1, len(text2)+1):
            prev = dp[0]
            for j in range(1, len(text1)+1):
                tmp = dp[j]
                if text2[i-1] == text1[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(tmp, dp[j-1])
                prev = tmp
        return dp[-1]


if __name__ == '__main__':
    str1 = 'abcde'
    str2 = 'ace'
    solution = Solution()
    max_sub = solution.longestCommonSubsequence_dynamic_planning1(str1, str2)
    pass
