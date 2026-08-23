class Solution:
    def isAcronym(self, words, s):
        return ''.join(word[0] for word in words) == s