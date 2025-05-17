class Solution(object):
    def lengthOfLastWord(self, s):
        i=len(s)-1
        lenoflw=0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            lenoflw+=1
            i-=1
        return lenoflw
        