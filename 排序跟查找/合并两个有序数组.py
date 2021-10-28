from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        elif n > 0:
            i, j = 0, 0
            while i < m and j < n:
                if nums2[j] > nums1[i]:
                    i += 1
                else:
                    nums1[i+1:m+1] = nums1[i:m]
                    nums1[i] = nums2[j]
                    j += 1
                    m += 1
            nums1[m:] = nums2[j:]


if __name__ == '__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    pass
