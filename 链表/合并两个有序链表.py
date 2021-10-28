from create_line import create_line, ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        node_list = []
        while l1 != None and l2 != None:
            node_list.append(l1)
            node_list.append(l2)
            l1 = l1.next
            l2 = l2.next
        while l1 != None: 
            node_list.append(l1)
            l1 = l1.next
        while l2 != None: 
            node_list.append(l2)
            l2 = l2.next
        node_list = sorted(node_list, key=lambda x: x.val)
        merge_node = node_list[0]
        p = merge_node
        for i in range(1, len(node_list)):
            p.next = node_list[i]
            p = p.next
        p.next = None
        return merge_node


if __name__ == '__main__':
    solution = Solution()
    n1 = [5]
    n2 = [1, 3, 4]
    line1 = create_line(n1)
    line2 = create_line(n2)
    merge_node = solution.mergeTwoLists(line1, line2)
    pass