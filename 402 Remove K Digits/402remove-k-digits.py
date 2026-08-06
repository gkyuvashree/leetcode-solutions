class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and i<stack[-1] and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        while stack and k>0:
            stack.pop()
            k-=1
        result=''.join(stack).lstrip('0')
        if result:
            return result
        else:
            return "0"