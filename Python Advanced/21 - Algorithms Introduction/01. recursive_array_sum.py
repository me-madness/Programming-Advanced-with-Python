def calc_sums(nums, idx=0):
    if idx == len(nums) - 1:
        return nums(idx)
    
    return nums[idx] + calc_sums(nums, idx + 1)


nums = [int(x) for x in input().split()]
print(calc_sums(nums))