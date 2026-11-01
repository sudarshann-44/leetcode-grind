# https://leetcode.com/problems/student-attendance-record-i/?envType=problem-list-v2&envId=string
#  Beats 100 % first try yeahhh

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find("LLL") > -1:
            return False
        if s.count("A") >= 2:
            return False
        return True