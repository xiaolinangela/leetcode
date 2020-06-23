def searchBST(root, val):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.val == val:
            return node
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return None
