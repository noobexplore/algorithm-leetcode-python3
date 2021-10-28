from create_line import create_line, ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''非递归版，双指针'''
        if l1 is None:
            return None
        if l2 is None:
            return None
        p1 = l1
        p2 = l2
        dummy = ListNode(0)  # 头结点
        p3 = dummy
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if p1 != None:
            p3.next = p1
        if p2 != None:
            p3.next = p2
        return dummy.next
    
    def mergeTwoLists_recur(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''递归版'''
        # 递归出口
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # 递归主体
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_recur(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recur(l1, l2.next)
            return l2
        
 

if __name__ == '__main__':
    n1 = [1, 2, 5]
    n2 = [1, 3, 4]
    l1 = create_line(n1)
    l2 = create_line(n2)
    solution = Solution()
    merge = solution.mergeTwoLists_recur(l1, l2)
    pass        
        
        