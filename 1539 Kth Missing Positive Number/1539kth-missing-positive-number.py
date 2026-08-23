class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        normal = set(range(1, max(arr) + k + 1))
        missings = normal - set(arr)
        list_missings = sorted(list(missings))
        return list_missings[k - 1]