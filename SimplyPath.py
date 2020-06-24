def simplifyPath(path):
    stack = []
    for portion in path.split("/"):
        if portion == "..":
            stack.pop()
        elif portion == "." or not portion:
            continue
        else:
            stack.append(portion)
    final_str = "/" + "/".join(stack)
    return final_str


if __name__ == "__main__":
    path = "/a//b////c/d//././/.."
    print(simplifyPath(path))


# Time Complexity: O(n)
# Space Complexity: O(n)
