import time
from typing import List


class Solution():
    def findMaxSequence(self, n: List[int]) -> int:
        '''
        题目描述，求例如[1, 5, 2, 3, 4]数组的最长递增子序列的最大长度[1, 2, 3, 4]
        '''
        # 暴力求解版本

        def get_SeqLength(L: List[int], index: int) -> int:
            # 递归出口
            if index == len(L) - 1:
                return 1
            
            max_seq = 1
            for i in range(index+1, len(L)):
                if L[i] > L[index]:
                    max_seq = max(get_SeqLength(L, i) + 1, max_seq)
            
            return max_seq
        
        return max([get_SeqLength(n, j) for j in range(len(n))])

    def findMaxSequence_bydict(self, n: List[int]) -> int:
        '''
        题目描述，求例如[1, 5, 2, 3, 4]数组的最长递增子序列的最大长度[1, 2, 3, 4]
        '''
        # 利用一个字典保存已经求得的中间结果
        memo = {}
        def get_SeqLength(L: List[int], index: int) -> int:
            # 先判断是否求得过到index的路径如果有直接返回
            if index in memo.keys():
                return memo[index]
            # 递归出口
            if index == len(L) - 1:
                return 1
            
            max_seq = 1
            for i in range(index+1, len(L)):
                if L[i] > L[index]:
                    max_seq = max(get_SeqLength(L, i) + 1, max_seq)
            memo[i] = max_seq
            return max_seq
        
        return max([get_SeqLength(n, j) for j in range(len(n))])

if __name__ == "__main__":
    start = time.time()
    n = [1, 5, 2, 3, 4]
    solution = Solution()
    maxseq = solution.findMaxSequence(n)
    end = time.time() - start
