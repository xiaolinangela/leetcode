# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guessNumber(n):
    while guess(n) == -1:
        n = n // 2
        low = n
        high = n * 2
        if guess(low) == 0:
            return low
        if guess(high) == 0:
            return high
        while True:
            mid = (low+high) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid
            else:
                low = mid


# Time Complexity O(logn)
# Space Complexity O(1)
