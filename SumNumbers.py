# recursive
def sumNumbers(root):
    def preorder(r, curr_number):
        nonlocal root_to_leaf
        if r:
            curr_number = curr_number*10 + r.val
            if not r.left and not r.right:
                root_to_leaf += curr_number

            preorder(r.left, curr_number)
            preorder(r.right, curr_number)

    root_to_leaf = 0
    preorder(root, 0)
    return root_to_leaf
# Time Complexity O(N)
# Space Complexity O(H) H is the height


# iterative
def sumNumber(root):
    stack = [(root, 0)]
    root_to_leaf = 0
    while stack:
        r, curr = stack.pop()
        curr = curr*10 + r.val
        if not r.left and not r.right:
            root_to_leaf += curr
        else:
            if r.left:
                stack.append((r.left, curr))
            if r.right:
                stack.append((r.right, curr))
    return root_to_leaf
# Time Complexity O(N)
# Space Complexity O(H) H is the height
