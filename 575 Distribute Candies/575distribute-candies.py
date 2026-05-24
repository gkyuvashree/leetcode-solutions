class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m = len(set(candyType))
        n = len(candyType) // 2
        return min(m,n)
        