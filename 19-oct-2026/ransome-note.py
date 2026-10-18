# Problem : https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for letter in ransomNote:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        for letter in magazine:
            if letter in hashmap.keys():
                hashmap[letter] = hashmap.get(letter, 0) - 1

        result = True
        for value in hashmap.values():
            if value > 0:
                result = False
        return result
        