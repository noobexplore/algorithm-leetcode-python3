import math

class Solution:
    def countPrimes(self, n: int) -> int:
        """埃筛法"""
        count = 0
        # 先初始化n的数组全部值为True
        isPrimes = [True for _ in range(n)]
        sq = int(math.sqrt(n))
        for i in range(2, sq):
            for j in range(i**2, n, i):
                # 核心为以上如何标记合数
                if isPrimes[i]:
                    isPrimes[j] = False
        # 然后最终计数数组中为true的个数
        for p in range(2, n):
            count += isPrimes[p]
        return count

if __name__ == '__main__':
    n = 20
    solution = Solution()
    cp = solution.countPrimes(n)
    pass