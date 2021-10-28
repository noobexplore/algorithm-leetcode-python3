from typing import List
from create_tree import create_tree, TreeNode

class Solution:
    
    def sortedArrayToBST_recur(self, n: List[int]):
        if len(n) == 0:
            return None
        mid = len(n) // 2
        root = TreeNode(n[mid])
        root.left = self.sortedArrayToBST_recur(n[:mid])
        root.right = self.sortedArrayToBST_recur(n[mid+1:])
        return root
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        尝试用分治的思路，感觉还是要递归
        '''
        return self.sortedArrayToBST_recur(nums)
    

if __name__ == '__main__':
    solution = Solution()
    n = [-10,-3,0,5,9]
    root = solution.sortedArrayToBST(n)
    pass
        
        
            
        