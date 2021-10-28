from create_line import create_line_cycle, ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        head_dict = {}
        while head:
            if head not in head_dict:
                head_dict[head] = 1
            else:
                return True
            head = head.next
        return False


if __name__ == '__main__':
    n = [3, 2, 0, 4]
    head = create_line_cycle(n, 1)
    solution = Solution()
    result = solution.hasCycle(head)
    pass