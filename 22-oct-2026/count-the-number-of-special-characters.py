# Problem https://leetcode.com/problems/count-the-number-of-special-characters-i

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = "".join(set(word))
        special_chars = 0
        hashmap = {key: 0 for key in word if key.lower() == key}
        for i in range(len(word)):
            if word[i].upper() == word[i] and hashmap.get(word[i].lower(), None) != None:
                special_chars +=1
        return special_chars
        