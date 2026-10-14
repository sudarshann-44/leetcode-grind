# Problem link : https://leetcode.com/problems/longest-common-prefix/?envType=problem-list-v2&envId=array

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        for i in range(len(first)):
            compare_char = first[i]
            for j in range(1, len(strs)):
                if i < len(strs[j]) and strs[j][i] == compare_char:
                    continue
                else:
                    return first[:i]
        return first