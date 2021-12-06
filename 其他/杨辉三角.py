"""给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        动态规划：
        1. 理解题意：
            - 生成的对应矩阵维度为[[1], [2], [3], ... , [n]]
            - 每个行起始为1中间值全部为上一行中的前一列的值加上当前列的值的和
        2. 确定状态:
            - dp[i][j]为当前矩阵对应的值
        3. 状态转移矩阵：
            - dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        4. 边界确定：
            - dp[i][0] = 1
        5. 返回的值：
            - dp中需要去除掉为0的值
        6. 优化的点：
            - 如何动态的确定维度
        '''
        # 初始化全部为统一维度nxn的矩阵
        dp = [[0 for _ in range(numRows)] for _ in range(numRows)]
        res = [[1] for _ in range(numRows)]
        # 初始化dp[i][0] = 1
        for i in range(numRows):
            dp[i][0] = 1
        # 开始进行状态转移计算
        for i in range(1, numRows):
            for j in range(1, numRows):
                if dp[i-1][j-1] != 0 or dp[i-1][j] != 0:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    res[i].append(dp[i-1][j-1] + dp[i-1][j])
        return res
    
    def generate_list(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp = [1]*(i+1)
            for j in range(1, i):
                if j == i:
                    continue
                temp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(temp)
        return res
                    
                    
                

if __name__ == "__main__":
    n = 5
    solution = Solution()
    dp = solution.generate_list(n)
    pass
        