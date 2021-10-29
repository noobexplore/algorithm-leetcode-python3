from typing import List


class TreeNode:
    '''初始化树节点'''

    def __init__(self, root=0, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right


def createTree(treeList: List[int]) -> TreeNode:
    '''输入的层序遍历数组'''
    queue_node = []
    n = len(treeList)
    if n == 0:
        return None
    if treeList[0] != None:
        root = TreeNode(treeList[0])
        queue_node.append(root)  # 入队列
    i = 0
    while len(queue_node) > 0:
        if 2*i+1>=n:
            break
        T = queue_node.pop(0)  # 出列
        # 处理左子树
        if treeList[2*i+1] == None:
            T.left = None
        else:
            T.left = TreeNode(treeList[2*i+1])
            queue_node.append(T.left)
        # 处理右子树
        if treeList[2*i+2] == None:
            T.right = None
        else:
            T.right = TreeNode(treeList[2*i+2])
            queue_node.append(T.right)
        i += 1
    return root


if __name__ == '__main__':
    n = [3, 9, 20, None, None, 5, 7]
    root = createTree(n)
    pass