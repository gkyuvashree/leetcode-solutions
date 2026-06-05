class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        ans=[-1]*n
        for i in range(2*n):
            idx=i%n
            while stack and nums[idx]>nums[stack[-1]]:
                b=stack.pop()
                ans[b]=nums[idx]
            if i<n:
                stack.append(idx)
        return ans