from create_line import ListNode, create_line

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        g = head
        p = head
        nums = 0
        count = 0
        while g.next != None: 
            nums += 1
            g = g.next
        if nums-n <= 0:
            return p.next.next
        while p.next != None:
            if count == nums-n:
                p.next = p.next.next
                return head
            p = p.next
            count += 1
        return head




if __name__ == '__main__':
    solution = Solution()
    test = [1]
    head = create_line(test)
    head = solution.removeNthFromEnd(head, 1)
    pass
    