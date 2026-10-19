# https://leetcode.com/problems/reverse-degree-of-a-string/?envType=daily-question&envId=2026-10-19

import string

class Solution:
    def reverseDegree(self, s: str) -> int:
        a_to_z_dict = {letter: index for letter, index in zip(string.ascii_lowercase, range(26, 0, -1))}
        product = 0
        for i in range(len(s)):
            product += a_to_z_dict[s[i]] * (i + 1)
        return product
