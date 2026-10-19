# Problem : https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        collection = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0;
        right = len(s) - 1
        while left < right:
            if s[left] in collection and s[right] in collection:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in collection:
                left +=1
            else:
                right -= 1
        return "".join(s)

