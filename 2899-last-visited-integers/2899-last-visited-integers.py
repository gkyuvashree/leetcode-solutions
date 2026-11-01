class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0

        for i in nums:
            if i > 0:
                seen.insert(0, i)
                k = 0
            else:
                k += 1

                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)

        return ans