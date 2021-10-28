from create_tree import createTree, TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left_node_num = self.maxDepth(root.left) + 1
        right_node_num = self.maxDepth(root.right) + 1

        return max(left_node_num, right_node_num)

if __name__ == '__main__':
    n = [3, 9, 20, None, None, 15, 7]
    tree = createTree(n)
    solution = Solution()
    dep = solution.maxDepth(tree)
    pass