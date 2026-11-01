# Problem : https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution(object):
    def reverseWords(self, s):
        ans = ""
        splitted = s.split(" ")
        for i in range(len(splitted)):
            ans += splitted[i][::-1]
            if (i != len(splitted) - 1):
                ans += " "
        return ans