import copy
from typing import List


def maxSubArray(nums:List[int]) -> int:
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i] + max(dp[i-1], 0)
    return max(dp)

def maxSubArray_v1(nums:List[int]) -> int:
    n = len(nums)
    dp = nums[0]
    maxnums = dp
    for i in range(1, n):
        dp = nums[i] + max(dp, 0)
        maxnums = max(maxnums, dp)
    return maxnums

if __name__ == '__main__':
    nums = [-1]
    print(maxSubArray_v1(nums))