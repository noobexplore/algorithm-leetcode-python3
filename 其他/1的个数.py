class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


if __name__ == '__main__':
    n = 6
    solution = Solution()
    cc = solution.hammingWeight(n)
    pass