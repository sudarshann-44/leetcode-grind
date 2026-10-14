

# Problem link : https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2147483648
        MAX_INT =  2147483647
        negative = False
        if x < 0 :
            negative = True
            x = abs(x)
        listing = list(str(x))[::-1]
        final = ""
        for i in listing:
            final +=i
        if negative:
            final = int("-" + final)

        if final < MIN_INT or final > MAX_INT:
            return 0
        else:
            return final
        