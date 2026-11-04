# https://leetcode.com/problems/uncommon-words-from-two-sentences
# beats 100% on own lets goo 

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        entire_string = (s1 + " " + s2).split(" ")
        words = []
        hashmap = {} 
        for word in entire_string:
            hashmap[word] = hashmap.get(word, 0) + 1
        for obj in hashmap.items():
            if obj[1] == 1:
                words.append(obj[0])
        return words

sol = Solution()
print(sol.uncommonFromSentences("this apple is sweet", "this apple is sour"))