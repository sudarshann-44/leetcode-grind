# problem : https://leetcode.com/problems/merge-strings-alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 == "":
            return word2
        if word2 == "":
            return word1
        longest = len(word1)
        if len(word2) > len(word1):
            longest = len(word2)
        final_string = ""
        for i in range(longest):
            if i < len(word1):
                final_string += word1[i]
            if i < len(word2):
                final_string += word2[i]
        return final_string


        