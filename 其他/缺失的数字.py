from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_nums = len(nums)
        nomal = [i for i in range(max_nums+1)]
        num = set(nomal) - set(nums)
        return list(num)[0]
    

if __name__ == "__main__":
    nums = [3,0,1]
    solution = Solution()
    n = solution.missingNumber(nums)
    pass
