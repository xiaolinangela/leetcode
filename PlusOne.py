def plusOne(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


if __name__ == "__main__":
    a = [1, 2, 3]
    print(plusOne(a))

# Time Complexity O(N)
# Space Complexity O(1)
