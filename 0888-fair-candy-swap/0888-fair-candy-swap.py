
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a = sum(aliceSizes)
        b = sum(bobSizes)

        diff = (a - b) // 2

        for x in aliceSizes:
            y = x - diff
            if y in bobSizes:
                return [x, y]
