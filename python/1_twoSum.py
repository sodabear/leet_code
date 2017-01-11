# -*- coding: utf-8 -*-
# key is the to check if current element's complement
# is already existed inside the table

# in the dictionary keys are value of nums
# values are index
def twoSum(nums,target):
    dic = {}
    for x in range(len(nums)):
        complement = target - nums[x]
        if complement in dic:
            return [x, dic[complement]]
        #按顺序存入 dictionary
        dic[nums[x]] = x #不要用complement做key,complement是我检查的目标
    return 0


# Test case
nums_1 = [2, 7, 11, 15]
target_1 = 9
print("we want to show [0,1] and we got:", twoSum(nums_1,target_1))

