# Problem : https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        first = [i for i in nums1_set if i not in nums2_set]
        second = [i for i in nums2_set if i not in nums1_set]
        return [first, second]