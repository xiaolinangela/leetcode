def find_duplicates1(nums):
    nums.sort()
    output = []
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            output.append(nums[i])
            i += 1
    return output


def find_duplicated2(nums):
    d = {}
    output = []
    for i in nums:
        if i in d:
            output.append(i)
        else:
            d[i] = 1
    return output

# Method 1 - Space Complexity: O(1) Time Complexity: nLogn
# Method 2 - Space Complexity: O(n) Time Complexity: O(n) average case. O(n2) worst case
    # It takes a linear amount of time to iterate through the array.
    # ookups in a hashset are constant time on average, however those can degrade to linear time in the worst case. Note that an alternative is to use tree-based sets, which give logarithmic time lookups always.
