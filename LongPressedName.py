def isLongPressedName(name, typed):
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j == 0 or typed[j] != typed[j-1]:
            return False
    return i == len(name)


if __name__ == "__main__":
    name = "alex"
    typed = "aaleex"
    print(isLongPressedName(name, typed))


# Time Complexity O(N+M)
# Space Complexity O(1)
