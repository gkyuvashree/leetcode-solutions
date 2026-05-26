class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = []

        for num in nums:

            if a.count(num) < 2:
                a.append(num)

        for i in range(len(a)):
            nums[i] = a[i]

        return len(a)
