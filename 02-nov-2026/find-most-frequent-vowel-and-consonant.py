class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {}
        consonants = {} 
        vow = ['a', 'e', 'i', 'o', 'u']
        for data in s:
            if data in vow:
                vowels[data] = vowels.get(data, 0) + 1
            else:
                consonants[data] = consonants.get(data, 0) + 1
        vowels = list(sorted(vowels.items(), key=lambda item: item[1]))
        consonants = list(sorted(consonants.items(), key=lambda item: item[1]))
        if len(vowels) > 0 and len(consonants) > 0:
            return vowels[-1][1] + consonants[-1][1]
        else:
            if len(vowels) == 0:
                return consonants[-1][1]
            else:
                return vowels[-1][1]