# Problem : https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        for letter in t:
            hashmap[letter] = hashmap.get(letter, 0) - 1

        result = True
        for value in hashmap.values():
            if value != 0:
                result = False
        return result