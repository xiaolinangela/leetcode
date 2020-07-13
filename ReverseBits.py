def reverseBits(n):
    curr = n
    final = 0
    for i in range(32):
        last_bit = curr & 1
        curr = cur >> 1
        final += last_bit << (31-i)
    return final

# Time Complexity O(1)
# Space Complexity O(1)
