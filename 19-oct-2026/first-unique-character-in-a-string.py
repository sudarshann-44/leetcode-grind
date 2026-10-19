# problem : https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for elements in hashmap.items():
            if elements[1]== 1:
                return s.index(elements[0])

        return -1