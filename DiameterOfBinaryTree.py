def diameter_bt(root):
    ans = 0

    def depth(root):
        if not root:
            return 0
        left = depth(root.left)
        right = depth(root.right)
        ans = max(ans, left+right)
        return max(left, right) + 1
    depth(root)
    return ans


# Time Complexity O(N)
# Space Complexity O(N)
