class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []

        for i in range(len(s)):
            mini = float('inf')

            for j in range(len(s)):
                if s[j] == c:
                    mini = min(mini, abs(i - j))

            ans.append(mini)

        return ans