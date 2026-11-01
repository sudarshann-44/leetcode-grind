# Problem : https://leetcode.com/problems/reverse-string-ii/
# Beats 100% yeah...

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        limiter = 2 * k
        i = 0
        while True:
            current_split = s[i: i + limiter]
            if len(current_split) < k:
                ans += current_split[::-1]
                return ans
            else:
                ans += current_split[0: k][::-1] + current_split[k:]
            i+= limiter