class Solution:
    def revserseBits(self, n: int) -> int:
        """主要是熟悉python中对二进制位的操作"""
        res = 0
        for _ in range(32):
            # res统一往左移动一位
            res <<= 1
            # 腾出最后的位置用来装n的最后一位
            res += n & 1
            # 最后n再往右移动一位
            n >>= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 4294967293
    res = solution.revserseBits(n)
    pass
