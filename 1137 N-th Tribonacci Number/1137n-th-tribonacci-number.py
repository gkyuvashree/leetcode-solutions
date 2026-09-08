class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        prev3=0
        prev2=1
        prev1=1
        for i in range(3,n+1):
            current=prev1+prev2+prev3
            prev3=prev2
            prev2=prev1
            prev1=current
        return prev1
