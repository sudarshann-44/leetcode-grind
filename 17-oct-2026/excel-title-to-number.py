# problem : https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        AZ_dict = {char: seq  for char, seq in zip(string.ascii_uppercase, range(1,27))}
        if len(columnTitle) == 1:
            return AZ_dict[columnTitle]
        value = 0
        for letter, i in zip(list(columnTitle)[::-1], range(0, len(columnTitle))):
            value += AZ_dict[letter] * (26 ** (i))
        return value