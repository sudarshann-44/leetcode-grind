# problem : https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                ans+= s[i].upper()
                count += 1
                if (count == k):
                    ans += "-"
                    count = 0
        
        if len(ans) > 1 and ans[-1] == "-":
            ans = ans[:-1]
        return "".join(list(reversed(ans)))