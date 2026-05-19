class Solution(object):
    def repeatedSubstringPattern(self, s):
        a=(s+s)[1:-1]
        if s in a:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        