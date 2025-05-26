class Solution(object):
    def findGCD(self, nums):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        s=min(nums)
        l=max(nums)
        return gcd(s,l)
        