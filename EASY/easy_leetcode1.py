# 1. Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        numMap={}
        for index,val in enumerate(nums):
            remaining=target-val
            if remaining in numMap:
                return [numMap[remaining],index]
            else:
                numMap[val]=index

s = Solution()
print(s.twoSum([9, 2, 0, 5,4], 6))








