class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count

if __name__ == '__main__':
    x = 4
    y = 1
    solution = Solution()
    c = solution.hammingDistance(x, y)
    pass
