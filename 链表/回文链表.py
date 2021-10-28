from create_line import ListNode, create_line


class Solution:
    tmp = ListNode(None)

    def isPalindrome(self, head: ListNode) -> bool:
        '''递归版本'''
        self.tmp = head

        def check(node: ListNode):
            if node is None:
                return True
            result = check(node.next) and self.tmp.val == node.val
            self.tmp = self.tmp.next
            return result
        
        res = check(head)
        return res



if __name__ == '__main__':
    n = [1, 2, 2, 1]
    head = create_line(n)
    solution = Solution()
    res = solution.isPalindrome(head)
    pass