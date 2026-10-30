class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd

        count = Counter(deck)
        ans = 0

        for i in count.values():
            ans = gcd(ans, i)

        return ans >= 2