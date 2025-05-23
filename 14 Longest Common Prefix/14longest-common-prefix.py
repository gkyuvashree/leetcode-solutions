class Solution(object):
    def longestCommonPrefix(self, strs):
        a=""
        for i in range(len(strs[0])):
            for b in strs:
                if i ==len(b) or b[i]!=strs[0][i]:
                    return a
            a+=strs[0][i]
        return a
        