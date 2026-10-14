class Solution:

    def __init__(self):
        pass

    def is_anagram(self, anagram1, anagram2):
        hashmap = {}
        anagram1 = str(anagram1).replace(" ", "")
        anagram2 = str(anagram2).replace(" ", "")
        for letter in anagram1:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        print(hashmap)
        for letter in anagram2:
            if letter in hashmap:
                hashmap[letter] -= 1
            else:
                hashmap[letter] = 1 
        print(hashmap)
        return sum(hashmap.values()) == 0

    #incomplete



solution = Solution()
# print(solution.is_anagram("school master", "the classroom"))
print(solution.is_anagram("tea", "state"))