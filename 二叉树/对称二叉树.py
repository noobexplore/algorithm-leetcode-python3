from typing import List
from typing import List
from create_tree import TreeNode, create_tree


class Solution:
    result_list = None

    def isSymmetric_error(self, root: TreeNode) -> bool:
        self.result_list = []
        '''
        先中序遍历存储结果，然后再判断,
        这里面有bug，中序遍历如果是[1,2,2,2,None,2]这个方法就行不通
        '''
        self.midSearch(root)
        return self.isPalindrome(self.result_list)

    def isSymmetric_recur(self, root: TreeNode) -> bool:
        return self.isSymmetric_check(root.left, root.right)

    def isSymmetric_check(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 如果两个子树都为空则返回true
        if root1 == None and root2 == None:
            return True
        # 如果只有一个子树为空显然不成立
        if root1 == None or root2 == None:
            return False
        # 然后开始判断
        return root1.val == root2.val and \
            self.isSymmetric_check(root1.left, root2.right) and \
            self.isSymmetric_check(root1.right, root2.left)

    def isSymmetric_queue(self, root: TreeNode) -> bool:
        queue_node = []
        # 还是先判断
        if root == None:
            return True
        # 初始状态先将根节点的左右子树推入
        queue_node.append(root.left)
        queue_node.append(root.right)
        while len(queue_node) > 0:
            T1 = queue_node.pop(0)  # 弹出左子树
            T2 = queue_node.pop(0)  # 弹出右子树
            if T1 == None and T2 == None:
                continue  # 这里关键在于如果两边都为none函数要继续判断才行
            if T1 == None or T2 == None:
                return False
            if T1.val != T2.val:
                return False
            # 然后按照顺序入队
            queue_node.append(T1.left)
            queue_node.append(T2.right)
            queue_node.append(T1.right)
            queue_node.append(T2.left)
        return True
    


if __name__ == '__main__':
    n = [9,-42,-42,None,76,76,None,None,13,None,13]
    tree = create_tree(n)
    solution = Solution()
    result = solution.isSymmetric_queue(tree)
    pass
