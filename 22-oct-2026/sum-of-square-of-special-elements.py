# https://leetcode.com/problems/sum-of-squares-of-special-elements/?envType=daily-question&envId=2026-10-22

class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        special = 0
        n = len(nums)
        for i in range(0, len(nums)):
            if n % (i + 1) == 0:
                special += nums[i] ** 2
        return special