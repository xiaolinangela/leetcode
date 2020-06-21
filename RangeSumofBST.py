from collections import deque


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, L, R):
    q = deque([root])
    sum = 0
    while q:
        root = q.popleft()
        if root:
            if root.val >= L and root.val <= R:
                sum += root.val
            if root.val > L:
                q.append(root.left)
            if root.val < R:
                q.append(root.right)
    return sum


# Time Complexity: O(N) number of the nodes in the tree
# Space Complexity: O(H) where H is the height of the tree
