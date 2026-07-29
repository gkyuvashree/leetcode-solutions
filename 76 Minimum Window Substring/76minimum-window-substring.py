class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        count = 0
        ans = ""
        min_len = float('inf')

        for right in range(len(s)):
            if s[right] in need:
                need[s[right]] -= 1
                if need[s[right]] >= 0:
                    count += 1

            while count == len(t):
                if right - left + 1 < min_len:
                    ans = s[left:right+1]
                    min_len = right - left + 1

                if s[left] in need:
                    if need[s[left]] == 0:
                        count -= 1
                    need[s[left]] += 1

                left += 1

        return ans