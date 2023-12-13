#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for index,item in enumerate(nums):
            if target-item in hash:
                return [hash[target-item],index]
            hash[nums[index]]=index
# @lc code=end

