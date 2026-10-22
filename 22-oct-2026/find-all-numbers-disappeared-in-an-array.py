#  problem https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = [i for i in range(1, len(nums) + 1)]
        ans2 = []
        nums_set = set(nums)  # Build the set once

        for element in ans:
            if element not in nums_set:
                ans2.append(element)

        return ans2