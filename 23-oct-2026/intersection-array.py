# Problem : https://leetcode.com/problems/intersection-of-two-arrays/
# Solution bets 100 % yeah

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        first_set = set(nums1)
        second_set = set(nums2)
        if len(first_set) > len(second_set):
            return list(first_set.intersection(second_set))
        else:
            return list(second_set.intersection(first_set))