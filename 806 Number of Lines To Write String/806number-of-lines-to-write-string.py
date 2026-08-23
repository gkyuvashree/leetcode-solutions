class Solution:
    def numberOfLines(self, widths, s):
        lines = 1
        pixels = 0

        for ch in s:
            w = widths[ord(ch) - ord('a')]

            if pixels + w > 100:
                lines += 1
                pixels = w
            else:
                pixels += w

        return [lines, pixels]