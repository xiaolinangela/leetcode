def perfectSquares(n):
    squares = []
    i = 1
    while i**2 <= n:
        squares.append(i**2)
        i += 1
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for square in squares:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i-square]+1)
    return dp[i]


if __name__ == "__main__":
    n = 18
    print(perfectSquares(n))
