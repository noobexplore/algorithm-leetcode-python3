from create_tree import createTree, TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        最大路径和思路，存在如下几种情况：
        1. 只包含左右子树的路径；
        2. 包含根节点的路径；
        3. 最主要的一点是，需要排除负路径；
        '''
        self.path_maxVal = float('-inf')  # 初始路径值

        def max_path(node: TreeNode):

            if node is None:
                return float('-inf')

            el = max_path(node.left)
            er = max_path(node.right)

            self.path_maxVal = max(self.path_maxVal, node.root+max(0, el)+max(0, er), el, er)

            return node.root + max(el, er, 0)

        max_path(root)
        return self.path_maxVal
    

if __name__ == '__main__':
    n = [-10,9,20,None,None,15,7]
    tree = createTree(n)
    solution = Solution()
    maxval = solution.maxPathSum(tree)
    pass
