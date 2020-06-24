def maxSubArrayLen(nums, k):
    dic = {0: -1}
    max_length = 0
    summ = 0
    for i in range(len(nums)):
        summ += nums[i]
        if summ - k in dic and max_length < i - dic[summ-k]:
            max_length = i - dic[summ-k]
        if summ not in dic:
            dic[summ] = i
    return max_length


# sumo of [i:j+1] = k,     [:j+1] - [:i] = k
if __name__ == "__main__":
    nums = [1, -1, 5, -2, 3]
    print(maxSubArrayLen(nums, 3))
