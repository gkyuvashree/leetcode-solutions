class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        total = sum(nums)
        curr = 0
        result = []

        for num in nums:
            curr += num
            result.append(num)

            if curr > total - curr:
                break

        return result