# problem : https://leetcode.com/problems/roman-to-integer/
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_number = ""
        values = {
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            900: 'CM',
            400: 'CD',
            90: 'XC',
            40: 'XL',
            9: 'IX'
        }

        while num >= 1:
            # print(num)
            if num >= 1000:
                num -= 1000
                roman_number += values[1000]
            elif num >= 900:
                num -= 900
                roman_number += values[900]
            elif num >= 500:
                num -= 500
                roman_number += values[500]
            elif num >= 400:
                num -= 400
                roman_number += values[400]
            elif num >= 100:
                num -= 100
                roman_number += values[100]
            elif num >= 90:
                num -= 90
                roman_number += values[90]
            elif num >= 50:
                num -= 50
                roman_number += values[50]
            elif num >= 40:
                num -= 40
                roman_number += values[40]
            elif num >= 10:
                num -= 10
                roman_number += values[10]
            elif num >= 9:
                num -= 9
                roman_number += values[9]
            elif num >= 5:
                num -= 5
                roman_number += values[5]
            else:
                roman_number += values[num]
                num -= num
        return roman_number

sol = Solution()
print(sol.intToRoman(3749))