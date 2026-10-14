
# Problem : https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "" and t != "":
            return t;
        if t == "" and s != "":
            return s
        slist = list(s)
        tlist = list(t)
        short_string = tlist
        long_string = slist
        if len(s) < len(t):
           short_string = slist
           long_string = tlist

        for i in short_string:
            del long_string["".join(long_string).find(i)]

        return "".join(long_string) 


#  Optimized

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]

        return list(count.keys())[0]
