# Problem : https://leetcode.com/problems/unique-number-of-occurrences
# beats time of 100% and space of 94% yeahhhhhh
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashmap = {}
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        return len(hashmap.values()) == len(set(hashmap.values()))
        