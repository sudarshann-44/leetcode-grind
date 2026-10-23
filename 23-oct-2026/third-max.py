# https://leetcode.com/problems/third-maximum-number/
# Solution bets 100 % yeah


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(sorted(set(nums)))
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[1]
        else:
            return nums[-3]
        