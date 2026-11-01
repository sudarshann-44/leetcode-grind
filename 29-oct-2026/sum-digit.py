# https://leetcode.com/problems/add-digits/
# beats 100 % yeah 

class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        while True:
            summation = sum(list(map(int, str(num))))
            if len(str(summation)) == 1:
                return summation
            num = summation