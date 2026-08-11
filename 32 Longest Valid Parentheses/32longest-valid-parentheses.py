class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0
        stack=[-1]
        for i in range(len(s)):
            ch=s[i]
            if ch=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans=max(ans,i-stack[-1])
        return ans