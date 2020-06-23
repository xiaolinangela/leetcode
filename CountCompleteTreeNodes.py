from collections import deque


def countNodes(root):
    if not root:
        return 0
    queue = deque([root])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count
