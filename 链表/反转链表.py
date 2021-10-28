from create_line import create_line, ListNode


class Solution:
    '''
    反转链表的4种方式：
    1. 暴力求解，思路是利用列表进行保存值之后再利用头插法生成链表，即可进行反转；
    2. 堆栈求解，利用堆栈先进后出的特性，将值取出放入堆栈里面，在进行生成新链表；
    '''

    def reverseList_brute(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        p = head
        result = []
        while p is not None:
            result.append(p.val)
            p = p.next
        '''尾插法构建链表'''
        nums = len(result)
        i = nums - 2
        s = ListNode(result[-1], None)
        q = s
        while i >= 0:
            ne = ListNode(result[i], None)
            q.next = ne
            q = q.next
            i -= 1
        return s

    def reverseList_stack(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        stack_val = []
        p = head
        while p is not None:
            stack_val.append(p.val)
            p = p.next
        # 重构链表
        head = ListNode(stack_val.pop())
        q = head
        while len(stack_val) > 0:
            s = ListNode(stack_val.pop())
            q.next = s
            q = q.next
        return head

    def reverseList_double_point(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        newNode = None
        while head != None:
            tmpNode = head.next
            # 指向新的节点
            head.next = newNode
            # 移动新的节点
            newNode = head
            # 接上原来的节点
            head = tmpNode
        return newNode

    def reverseList_recur(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        # 递归前的逻辑处理，把每部反转前的节点存储下来
        newNode = head.next
        # 开始递归
        reverseNode = self.reverseList_recur(head.next)
        # 递归后的逻辑处理，将存储下来的节点再拼接上去
        newNode.next = head
        # 最后尾部要指向None避免呈环状
        head.next = None
        return reverseNode


if __name__ == '__main__':
    solution = Solution()
    n = [1, 2, 3, 4, 5]
    head = create_line(n)
    reverse = solution.reverseList_recur(head)
    pass
