# problem : https://leetcode.com/problems/excel-sheet-column-title/

import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        AZ_dict = {seq: char for char, seq in zip(string.ascii_uppercase, range(0,27))}
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans += AZ_dict.get(columnNumber % 26)
            columnNumber = columnNumber // 26
        return ans[::-1]

        