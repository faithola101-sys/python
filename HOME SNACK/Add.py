def sum_first_middle_last(nums):  
    if len(nums) == 0:
        return 0
    first = nums[0]
    middle = nums[len(nums) // 2]
    last = nums[-1]
    total = first + middle + last
    return total

nums = [5, 10, 15, 20, 25, 30, 35]
result = sum_first_middle_last(nums)
print(result)