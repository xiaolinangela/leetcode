def islandPerimeter(grid):
    m = len(grid)
    n = len(grid[0])
    p = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            else:
                temp = 0
                if j > 0:
                    if grid[i][j-1] == 1:
                        temp += 1
                if j < len(grid[0])-1:
                    if grid[i][j+1] == 1:
                        temp += 1
                if i < len(grid) - 1:
                    if grid[i+1][j] == 1:
                        temp += 1
                if i > 0:
                    if grid[i-1][j] == 1:
                        temp += 1
                p += (4-temp)
    return p


if __name__ == "__main__":
    l = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(islandPerimeter(l))


# Time Complexity O(MN)
# Space Complexity O(1)
