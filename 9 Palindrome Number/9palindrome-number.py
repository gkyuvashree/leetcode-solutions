class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x==0:
            return True
        if x%10==0:
            return False
        org=x
        rev=0
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if rev==org:
            return True
        return False