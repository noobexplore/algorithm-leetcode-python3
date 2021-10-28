from typing import List
from collections import deque
from create_tree import createTree, TreeNode


class Solution:
    recur_list = []
    '''递归前中后序'''

    def preOrder_recur(self, root: TreeNode) -> List:
        if root is None:
            return root
        self.recur_list.append(root.root)
        self.preOrder_recur(root.left)
        self.preOrder_recur(root.right)
        return self.recur_list

    def divide_recur(self, root: TreeNode) -> List:
        '''与上述至上而下的思路不一样，分治法是至底向上'''
        if root is None:
            return []
        left_list = self.divide_recur(root.left)
        right_list = self.divide_recur(root.right)
        return [root.root] + left_list + right_list

    def inOrder_recur(self, root: TreeNode) -> List:
        if root is None:
            return root
        self.inOrder_recur(root.left)
        self.recur_list.append(root.root)
        self.inOrder_recur(root.right)
        return self.recur_list

    def postOrder_recur(self, root: TreeNode) -> List:
        if root is None:
            return root
        self.postOrder_recur(root.left)
        self.postOrder_recur(root.right)
        self.recur_list.append(root.root)
        return self.recur_list

    '''非递归前中后，统一利用栈进行处理，其中有些细节要注意'''

    def preOrder(self, root: TreeNode) -> List:
        stack = [root]  # 前序细节先根节点入栈
        preorder_list = []
        while len(stack) > 0:
            node = stack.pop()
            preorder_list.append(node.root)
            # 细节是先入右子树后入左子树
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return preorder_list

    def inOrder(self, root: TreeNode) -> List:
        inorder_list, stack = [], []
        node = root
        while len(stack) > 0 or node is not None:
            # 中序是先压栈再访问
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                # 走到这里说明左边走完了, 需要弹栈了
                node = stack.pop()
                inorder_list.append(node.root)
                node = node.right
        return inorder_list

    def postOrder(self, root: TreeNode) -> List:
        postorder_list, stack = [], []
        node = root
        last = None
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)  # 入栈
                node = node.left
            else:
                peek = stack[-1]
                # 判断有没有右节点的情况，并且有没有弹出过
                if peek.right is not None and last != peek.right:
                    # 没有弹出过的话就走右边
                    node = peek.right  # 细节走右边
                else:
                    last = stack.pop()  # 否则就弹栈
                    postorder_list.append(last.root)
        return postorder_list

    def level_order(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = deque([root])  # 初始化队列，根节点先入队
        while len(queue) > 0:
            level = []  # 每个层级都需要初始化
            queue_size = len(queue)
            for _ in range(queue_size):
                T = queue.popleft()  # 出队
                level.append(T.root)
                if T.left is not None:
                    queue.append(T.left)
                if T.right is not None:
                    queue.append(T.right)
            result.append(level)
        return result


if __name__ == '__main__':
    n = ["A", "B", "C", "D", "F", "E", None]
    tree = createTree(n)
    solution = Solution()
    divide_list = solution.divide_recur(tree)
    pass
