class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        ans = -1

        for i in freq:
            if i == freq[i]:
                ans = max(ans, i)

        return ans