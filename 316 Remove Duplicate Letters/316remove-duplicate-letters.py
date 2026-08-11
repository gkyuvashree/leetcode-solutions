class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            ch = s[i]

            if ch in stack:
                continue

            while stack and stack[-1] > ch and stack[-1] in s[i+1:]:
                stack.pop()

            stack.append(ch)

        return ''.join(stack)