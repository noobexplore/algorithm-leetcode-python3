import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        else:
            if n%3 == 0:
                return self.isPowerOfThree(n//3)
            else:
                return False
    
    def isPowerOfThree_log(self, n: int) -> bool:
        return (math.log10(n) / math.log10(3)) % 1 == 0 


if __name__ == '__main__':
    n = 27
    solution = Solution()
    flag = solution.isPowerOfThree_log(n)
    pass
        
