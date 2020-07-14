def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return sameTree(p.right, q.right) and sameTree(p.left and q.left)

# Time Complexity O(N)
# Space Complexity O(log(N))
