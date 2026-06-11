class Solution:
    def permute(self, nums):
        result = []

        def backtrack(idx):
            if idx == len(nums):
                result.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        backtrack(0)
        return result