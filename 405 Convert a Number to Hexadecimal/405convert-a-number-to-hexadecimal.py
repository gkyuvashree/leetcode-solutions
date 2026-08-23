class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        ans = ""

        if num < 0:
            num += 2**32

        while num:
            ans = hex_chars[num % 16] + ans
            num //= 16

        return ans