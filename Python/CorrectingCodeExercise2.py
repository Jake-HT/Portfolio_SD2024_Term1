def find_average(nums): 
    total = 0 
    count = 0 
    for num in nums: 
        total += nums[num-1] 
        count += 1 
    average = total / count 
    return average

print(find_average([1,2,3,4,5,6,7,8,9]))