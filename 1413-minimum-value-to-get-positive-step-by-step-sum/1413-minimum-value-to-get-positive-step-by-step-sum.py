class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        mini = 0

        for num in nums:
            total += num
            mini = min(mini, total)

        return 1 - mini