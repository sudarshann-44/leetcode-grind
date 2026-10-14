# Problem : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        for i in range(len(haystack)):
            if (i + needle_length - 1) < len(haystack):
                if haystack[i: i + needle_length] == needle:
                    return i
        return -1  

sol = Solution()
print(sol.strStr("hello", "ll"))



