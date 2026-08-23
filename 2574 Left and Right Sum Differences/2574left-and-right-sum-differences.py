class Solution:
    def leftRightDifference(self, nums):
        total = sum(nums)
        left = 0
        ans = []

        for n in nums:
            right = total - left - n
            ans.append(abs(left - right))
            left += n

        return ans