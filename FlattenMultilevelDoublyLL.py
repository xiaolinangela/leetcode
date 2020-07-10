class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head):
    if not head:
        return
    dummy = Node(0)
    prev = dummy
    stack = []
    stack.append(head)
    while stack:
        root = stack.pop()
        root.prev = prev
        prev.next = root
        if root.next:
            stack.append(root.next)
        if root.child:
            stack.append(root.child)
            root.child = None
        prev = root
    dummy.next.prev = None
    return dummy.next


# Time Complexity O(N)
# Space Complexity O(N)
