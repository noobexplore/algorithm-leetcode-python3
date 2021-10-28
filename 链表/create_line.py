from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_line(n:List[int]) -> ListNode:
    '''尾插法构建链表'''
    i = 1
    nums = len(n)
    s = ListNode(n[0], None)
    p = s
    while i<nums:
        ne = ListNode(n[i], None)
        p.next = ne
        p = p.next
        i += 1
    return s

def create_line_cycle(n:List[int], pos:int) -> ListNode:
    '''尾插法构建循环链表'''
    i = 1
    nums = len(n)
    s = ListNode(n[0], None)
    p = s
    while i<nums: 
        ne = ListNode(n[i], None)
        p.next = ne
        if i == pos:
            q = ne
        p = p.next
        i += 1
    p.next = q
    return s


