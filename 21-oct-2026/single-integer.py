# problem : https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hashmap = {}
        for element in nums: 
            hashmap[element] = hashmap.get(element, 0) + 1
        for item in hashmap.items():
            if item[1] == 1:
                return item[0]