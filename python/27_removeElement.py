# -*- coding: utf-8 -*-

def removeElement(nums,val):
    hi,lo = len(nums)-1,0
    while lo <= hi:
        if nums[lo] == val:
            nums[lo] = nums[hi]
            hi -=1
        else:
            lo +=1
    return lo+1

def removeElement_1(nums,val):
    m = 0
    for x in range(len(nums)):
        if nums[x] != val:
            nums[m] = nums[x]
            m +=1
    return m




#test
nums_1 = [1,2,3,4,2,1,2]
val_1 = 2
val_2 = 1

print(removeElement(nums_1,val_1))
print(removeElement_1(nums_1,val_1))