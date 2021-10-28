import sys
from create_tree import TreeNode, create_tree

class Solution:
    prev = TreeNode()
    def isValidBST_recur(self, root:TreeNode) -> bool:
        '''递归版'''
        return self.isVaildBST_check(root, -sys.maxsize, sys.maxsize)
    
    def isVaildBST_check(self, node:TreeNode, min_val, max_val):
        if node == None:
            '''默认node为空的时候返回正确'''
            return True
        if node.val <= min_val or node.val >= max_val:
            '''
            这里的判断是关键，只需要去判断左右子树与根节点的关系就OK
            '''
            return False
        
        return self.isVaildBST_check(node.left, min_val, node.val) and self.isVaildBST_check(node.right, node.val, max_val)
    
    def isVaildBST_midSearch(self, root:TreeNode):
        if root == None:
            '''默认为空的时候返回true'''
            return True
        # 中序走左子树
        if not self.isVaildBST_midSearch(root.left):
            return False
        if self.prev != None and self.prev.val >= root.val:
            return False
        # 保存前一节点
        self.prev = root
        # 中序走右子树
        if not self.isVaildBST_midSearch(root.right):
            return False
        return True
        
    
    
if __name__ == '__main__':
    solution = Solution()
    n = [5, 3, 7, 1, 4, 6, 8]
    tree = create_tree(n)
    result = solution.isVaildBST_midSearch(tree)
    pass