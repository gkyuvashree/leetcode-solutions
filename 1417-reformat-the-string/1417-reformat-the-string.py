class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []

        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)

        if abs(len(digits) - len(letters)) > 1:
            return ""

        if len(digits) > len(letters):
            digits, letters = digits, letters
        else:
            digits, letters = letters, digits

        result = ""

        for i in range(len(digits)):
            result += digits[i]
            if i < len(letters):
                result += letters[i]

        return result