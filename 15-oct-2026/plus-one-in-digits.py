# Problem : https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        letters = ""
        for digit in digits:
            letters += str(digit)
        increments = int(letters) + 1
        final = []
        for letter in str(increments):
            final.append(int(letter))
        return final


