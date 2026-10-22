
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        start = 0

        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == i:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[i]))

                start = i + 1

        return ans
