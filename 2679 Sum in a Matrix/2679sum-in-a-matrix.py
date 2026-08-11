class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        rows=len(nums)
        cols=len(nums[0])
        ans=0
        for j in range(cols):
            maximum=0
            for i in range(rows):
                maximum=max(maximum,nums[i][j])
            ans+=maximum
        return ans
        