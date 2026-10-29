
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)

        nums.remove(largest)

        if all(largest >= 2 * x for x in nums):
            return index
        return -1
