class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""

        for i in range(len(s)):
            if s[i].isdigit():
                result += chr(ord(s[i - 1]) + int(s[i]))
            else:
                result += s[i]

        return result