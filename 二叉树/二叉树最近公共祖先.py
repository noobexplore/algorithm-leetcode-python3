from create_tree import TreeNode, createTree

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        递归思路：
        1. 找那个根节点同时包含p；
        2. q节点也有可能是p包含q；
        3. p节点包含q；
        '''
        
        # 递归前
        if root is None:
            # 叶子节点
            return None
        
        # 包含q或者p就返回
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)  # 开始走右边
        right = self.lowestCommonAncestor(root.right, p, q)  # 开始走左边

        '''
        递归后有三种情况:
        1. p,q分别在两侧存在，那么就返回根节点；
        2. 同时在左侧即是右为空，那么就返回左节点；
        3. 同时在右侧即是左为空，那么就返回右节点；
        '''
        if left is not None and right is not None:
            return root
        if left is None and right is None:
            return None
        if left is not None:
            return left
        if right is not None:
            return right


if __name__ == '__main__':
    n = [3,5,1,6,2,0,8,None,None,7,4]
    solution = Solution()
    tree = createTree(n)
    p, q = TreeNode(7), TreeNode(4)
    root = solution.lowestCommonAncestor(tree, p, q)
    pass