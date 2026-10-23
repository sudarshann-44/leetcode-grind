# Problem : https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashmap = {}
        for index, value in enumerate(nums):
            if hashmap.get(value, None) == None:
                hashmap[value] = index
            else:
                diff = abs(index - hashmap[value])
                if diff <= k:
                    return True
                hashmap[value] = index
        return False