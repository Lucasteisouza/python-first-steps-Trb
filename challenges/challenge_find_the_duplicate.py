def find_duplicate(nums):
    if len(nums) < 2:
        return False
    ordered_nums = sorted(nums)
    for i in range(len(ordered_nums) - 1):
        if type(ordered_nums[i]) != int or ordered_nums[i] < 0:
            return False
        if ordered_nums[i] == ordered_nums[i + 1]:
            return ordered_nums[i]
    return False
    raise NotImplementedError
