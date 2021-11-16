class linknode:
    def __init__(self, val=None, min_val=None, next=None):
        self.val = val
        self.min_val = min_val
        self.next = next


class MinStack:

    def __init__(self):
        self.head_node = linknode()

    def push(self, val: int) -> None:
        if self.head_node.next == None:
            self.head_node.next = linknode(val=val, min_val=val)
        else:
            min_val = self.head_node.next.min_val
            if val < min_val:
                self.head_node.next = linknode(
                    val=val, min_val=val, next=self.head_node.next)
            else:
                self.head_node.next = linknode(
                    val=val, min_val=min_val, next=self.head_node.next)

    def pop(self) -> None:
        if self.head_node.next == None:
            print('is empty')
        else:
            self.head_node.next = self.head_node.next.next

    def top(self) -> int:
        if self.head_node.next == None:
            return -1
        else:
            return self.head_node.next.val

    def getMin(self) -> int:
        return self.head_node.next.min_val

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    min_1 = minStack.getMin()
    minStack.pop()
    top_1 = minStack.top()
    min_2 = minStack.getMin()
    pass