import random
from copy import deepcopy
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_len = len(nums)

    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        self.random_num = random.randint(0, 200)
        temp = self.nums[:]
        for i in range(self.nums_len):
            temp[(i+self.random_num)%self.nums_len] = self.nums[i]
        return temp


if __name__ == '__main__':
    solution = Solution([1, 2, 3])
    print(solution.shuffle())
    print(solution.reset())
    print(solution.shuffle())
    print(solution.shuffle())
    print(solution.shuffle())
    pass
