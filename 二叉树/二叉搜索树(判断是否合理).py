from create_tree import createTree, TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return root
        tmp = root.root
        left_bool, right_bool = True, True
        # 走左子树
        left = self.isValidBST(root.left)
        if left != None:
            left_bool = left.root > tmp
        right = self.isValidBST(root.right)
        if right != None:
            right_bool = right.root < tmp
        return left_bool and right_bool


if __name__ == '__main__':
    n = [5, 1, 4, None, None, 3, 6]
    root = createTree(n)
    solution = Solution()
    isbst = solution.isValidBST(root)
    pass