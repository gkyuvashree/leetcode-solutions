class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))

        rank = {}

        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1

        ans = []

        for i in arr:
            ans.append(rank[i])

        return ans