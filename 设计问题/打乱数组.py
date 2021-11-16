import random
from copy import deepcopy
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_len = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle_1(self) -> List[int]:
        temp = self.nums[:]
        for i in range(1, self.nums_len):
            j = random.randint(0, i)
            # 这里进行交换
            temp[i] = temp[j]
            temp[j] = self.nums[i]
        return temp

    def shuffle_2(self) -> List[int]:
        temp = self.nums[:]
        for i in range(len(self.nums)-1, 0, -1):
            j = random.randint(0, i)
            temp[i], temp[j] = temp[j], temp[i]
        return temp


if __name__ == '__main__':
    solution = Solution([1, 2, 3])
    print(solution.shuffle_2())
    print(solution.reset())
    print(solution.shuffle_2())
    print(solution.shuffle_2())
    print(solution.shuffle_2())
    pass
