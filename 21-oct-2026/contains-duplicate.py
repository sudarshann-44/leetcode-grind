# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        return False
        