# problem : https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = []
        i = 0
        while i <= len(s) - 1:
            value = s[i]
            if i != len(s) - 1 and values.get(s[i]) < values.get(s[i + 1]):
                total.append(values.get(s[i + 1]) - values.get(s[i]))
                i+= 2
            else:
                total.append(values.get(value))
                i+=1
        return sum(total)