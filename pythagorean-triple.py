# input is an unsorted list of 3 positive integers

def pythagorean_triple(nums):
    nums.sort()
    return (nums[0]**2 + nums[1]**2) == nums[2]**2
