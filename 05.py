def twoSum(nums, target):
  # your code here
  sum = 0
  for j in range(len(nums)):
    sum = target - nums[j]
    for k in range(j+1,len(nums)):
     if nums[k] == sum :
        return [j, k]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9