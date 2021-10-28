from create_line import ListNode, create_line

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''双指针，主要是注意就删除头结点的情况 [1] 1 --> []'''
        first = ListNode(None, head)
        g = first
        p = first
        nums = 0
        count = 0
        while g.next != None: 
            nums += 1
            g = g.next
        if nums-n <= 0: # 这里判断为头结点的情况
            return p.next.next
        while p.next != None:
            if count == nums-n:
                p.next = p.next.next
                return first.next
            p = p.next
            count += 1
        return first.next

    def removeNthFromEnd_recur(self, head: ListNode, n: int) -> ListNode:
        '''递归版本'''
        def get_line_length(node: ListNode, n: int):
            '''获取链表的长度, 此处为获取链表长度的递归模板'''
            if node is None:
                return 0
            po = get_line_length(node.next, n) + 1
            if po == n + 1:
                node.next = node.next.next
            return po
        
        pos = get_line_length(head, n)
        if pos == n:
            return head.next
        return head

    def removeNthFromEnd_fast_slow(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # fast指针先走
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        # 然后再slow指针走
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        # 最后进行删除操作
        slow.next = slow.next.next
        return head

        
if __name__ == '__main__':
    solution = Solution()
    n = [1]
    head = create_line(n)
    head = solution.removeNthFromEnd_fast_slow(head, 1)
    pass
