# Problem : https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = set()
        while True:
            number = list(str(n))
            summation = 0
            for num in number:
                summation += int(num) ** 2
            if summation in seen:
                return False
            digit_sum = sum([int(i) for i in list(str(summation))])
            if digit_sum  == 1:
                return True
            else:
                seen.add(summation) 
                n = summation