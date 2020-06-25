def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return [i, dic[nums[i]]]
        else:
            dic[target-nums[i]] = i
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print(twoSum(nums, 9))
