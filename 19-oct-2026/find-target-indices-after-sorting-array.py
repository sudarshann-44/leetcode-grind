# Problem : https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        target_index = []
        nums = list(sorted(nums))
        for i in range(len(nums)):
            if nums[i] == target:
                target_index.append(i)
        return target_index