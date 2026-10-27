# Problem : https://leetcode.com/problems/reverse-words-with-same-vowel-count/
# Medium Difficulty
#  solved without help on first try yeahhh


class Solution:
    vowels = ["a", "e", "i", "o", "u"]

    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")

        if len(words) <= 1:
            return words[0]
        
        vowels_in_first_word = self.count_vowels(words[0])

        for i in range(1, len(words)):
            current_word = words[i]
            if len(current_word) >= vowels_in_first_word:
                if self.count_vowels(current_word) == vowels_in_first_word:
                    words[i] = current_word[::-1]

        return " ".join(words)


    def count_vowels(self, string: str) -> int:
        count = 0;
        for letter in string:
             if letter in self.vowels:
                 count += 1
        return count;

        
sol = Solution()
print(sol.reverseWords("cat and mice"))
print(sol.reverseWords("book is nice"))
print(sol.reverseWords("banana healthy"))