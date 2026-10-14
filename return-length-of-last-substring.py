# Problem : https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listing = s.split(" ")
        listing = [word for word in listing if word not in [" ", ""]]
        if len(listing) > 0:
            return len(listing[-1])
        else : 
            return None
        