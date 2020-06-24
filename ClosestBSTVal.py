def closetVal(tree, target):
    min_diff = float("inf")
    stack = []
     stack.append(root)
      result = root
       while stack:
            node = stack.pop()
            if abs(node.val-target) < min_diff:
                min_diff = abs(node.val-target)
                result = node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result.val

# Time Complexity O(N)
# Space Complexity O(N)
