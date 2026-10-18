# problem : https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        length = len(s) // 2
        for i in range(length):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        print(s)