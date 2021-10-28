from typing import List
from create_tree import create_tree, TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 先将根节点入队
        if root == None:
            return []
        queue_list = []
        queue_list.append(root)
        result_list = []
        while len(queue_list) > 0:
            level = []
            # 循环迭代对应每层的值
            for _ in range(len(queue_list)):
                T = queue_list.pop(0)
                if T.left != None:
                    queue_list.append(T.left)
                if T.right != None:
                    queue_list.append(T.right)
                level.append(T.val)
            result_list.append(level)
        return result_list
    

if __name__ == '__main__':
    n = [3,9,20,None,None,15,7]
    tree = create_tree(n)
    solution = Solution()
    result = solution.levelOrder(tree)
    pass
    