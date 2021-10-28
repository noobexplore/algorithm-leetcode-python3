from typing import List
from create_tree import TreeNode, create_tree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        递归思路，分治法的思路：
        1. 先求每个子树局部的高度
        2. 然后判断高度差
        3. 递归出口为走到root==None：
            - 那么高度差自然没有，也就自然为平衡二叉树
        '''

        def check_deth(node: TreeNode):
            if node is None:
                # 递归出口
                return 0, True

            # 往左求高度
            left_high, left_res = check_deth(node.left)
            # 往右求高度
            right_high, right_res = check_deth(node.right)
            # 求左右高度差进行判断
            result = abs(right_high-left_high) < 2
            return max(left_high, right_high) + 1, left_res and right_res and result

        _, res = check_deth(root)

        return res

    def post_order(self, root: TreeNode) -> List:
        '''
        利用stack进行一个后序遍历：
            - 核心点在于左子树弹出栈之后不能马上再弹出要判断下一个节点是否还有没有右子树
            - 有右子树还得将右子树压入栈之后再判断该节点是否弹出
        '''
        stack_node = []
        post_order = []
        last = None  # 该辅助变量用于
        node = root  # 游标指针进行辅助
        while len(stack_node) > 0 or node is not None:
            if node is not None:
                stack_node.append(node)
                node = node.left  # 一直走左子树
            else:
                # 说明左边走完了，马上开始走右边
                # 不过这里需要进行判断何时应该走右边所以需要一个辅助变量
                peek = stack_node[-1]  # 记录栈顶指针
                if peek.right is not None and last != peek.right:
                    node = peek.right  # 继续走右边
                else:
                    last = stack_node.pop()  # 弹出栈
                    post_order.append(last.val)
        return post_order
    
    def isBalanced_postLoop(self, root: TreeNode):
        '''
        基于后序遍历的思路
        核心点在于弹出栈的时候对于父节点的左右节点数的一个更新
        然后做差进行判断是否大于1
        '''
        stack_node = [[TreeNode(), -1, -1]]  # 这里有所区别是相当于递归调用的一个出口
        post_order = []
        node = root  # 游标指针进行辅助
        while len(stack_node) > 1 or node is not None:
            if node is not None:
                stack_node.append([node, -1, -1])
                node = node.left  # 一直走左子树
                if node == None:
                    # 左边为空，父节点更新左节点数为0
                    stack_node[-1][1] = 0
            else:
                peek = stack_node[-1][0]  # 还是需要一个peek记录栈顶指针
                if peek.right is not None and last != peek.right:
                    node = peek.right  # 这里没区别走右边
                else:
                    if peek.right is None:
                        # 如果右边指针也为空，更新父节点右节点数为0
                        stack_node[-1][2] = 0
                    # 然后弹出节点
                    last, dl, dr = stack_node.pop()
                    post_order.append(last.val)
                    if abs(dl - dr) > 1:
                        return False, post_order
                    # 然后开始比较节点数，取最大+1
                    d = max(dl, dr) + 1
                    # 再更新父节点的左右子树值，如果没有更新过的为-1的就说明是左边的值，否则右边
                    if stack_node[-1][1] == -1:
                        stack_node[-1][1] = d
                    else:
                        stack_node[-1][2] = d
        return True, post_order
                
                     
        


if __name__ == '__main__':
    n = [3, 9, 20, None, None, 15, 7]
    solution = Solution()
    tree = create_tree(n)
    res, post_list = solution.isBalanced_postLoop(tree)
    pass
