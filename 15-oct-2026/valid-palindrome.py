# Problem : https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        listing = []
        for element in list(s):
            if str.isalnum(element):
                listing.append(element.lower())
        original = "".join(listing)

        listing.reverse()
        return original == "".join(listing)
        