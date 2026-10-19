# problem : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        max_length = 0
        collection_parentesis = []
        for i in s:
            if i == "(":
                collection_parentesis.append(i)
                if max_length < len(collection_parentesis):
                    max_length += 1
            elif i == ")":
                collection_parentesis.pop()
        return max_length