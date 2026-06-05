class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        ans=[-1]*n
        for i in range(n):
            while stack and nums2[i]>nums2[stack[-1]]:
                a=stack.pop()
                ans[a]=nums2[i]
            stack.append(i)
        fa=[]
        for x in nums1:
            for i in range(n):
                if nums2[i]==x:
                    fa.append(ans[i])
                    break
        return fa