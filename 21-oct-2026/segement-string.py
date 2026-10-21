# Problem : https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        segments = [i for i in s.split(" ") if i not in ["", " "]]
        return len(segments)