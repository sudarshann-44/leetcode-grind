#  problem : https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(set(list(pattern))) != len(set(s.split(' '))):
            return False
        hashmap = {}
        for i,j in zip(list(pattern), s.split(' ')):
            hashmap[i] = j
        ans = []
        for pattern_letter in pattern:
            ans.append(hashmap[pattern_letter])
        return s == " ".join(ans)
                