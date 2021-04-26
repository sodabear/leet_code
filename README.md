# leet_code_done_right

## Goal
This repo is created to help people understand and inprove coding skill without their time by reading bad code. 
This title of the repo deserves a explanation. Most solutions on leetcode dicussion emphasis shortness. 
Those code are difficult to read, nonintuitive , abstraction barrier violated and suboptimal. 
Most importantly, They dont respect abstraction barrier. As Professor DeNero said "codes does not respect abstraction barrier 
should be through away". 


## Philosophie 
Most leetcode solution are in unreadable. 
My philisophie is to write clear and correct code for people to read. 

for example: 
https://discuss.leetcode.com/topic/22619/python-easy-to-understand-solution-o-n-n-time
why is this bad code? 
why can you add comment to indicate `if i > 0 and nums[i] == nums[i-1]:` is the why to remvoe duplicate?
Instead of using nested while lopp, why can you just use double for loop with binary search included? 

 ## Problem Review: 
 
 #1 Two Sum
 生成一个字典，和一对pairs，
 然后进行for loop
 字典里面存第一次出现的值和他的index
 
 #2 Add Two Numbers
 利用dummy node 和Carry node 
 定义循环结束的条件为 
 ```
 while l1 or l2  or carry 
 ```
 注意carry是对l1+l2+carry的总和 /10
 
 #3 Longest Substring Without Repeating Characters
 双指针，I和J的问题，遍历的时候要用index
 I后走，J先走，遇到重复的I+1，J不懂
