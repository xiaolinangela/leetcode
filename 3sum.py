def threeSum(nums):
    output = []
    found = set()
    dups = set()
    for i in range(len(nums)):
        if nums[i] not in dups:
            dups.add(nums[i])
            x = nums[i]
            htable = {}
            for j in range(i+1, len(nums)):
                y = nums[j]
                remainder = 0-x-y
                if remainder in htable:
                    max_val = max(x, y, remainder)
                    min_val = min(x, y, remainder)
                    if (min_val, max_val) not in found:
                        found.add((min_val, max_val))
                        output.append([x, y, remainder])
                htable[y] = j
    return output


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))


# Time Complexity O(n2)
# Space Complexity O(n2)
