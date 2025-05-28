class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        f=Counter(s) 
        values=list(f.values()) 
        return all(v==values[0] for v in values) 