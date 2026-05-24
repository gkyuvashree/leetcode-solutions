class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        c=nums[1]+nums[0]+nums[2]
        for i in range(len(nums)-1):
            l=i+1
            r=n-1
            while l<r:
                t=nums[l]+nums[r]+nums[i]
                if abs(target-t)<abs(target-c):
                    c=t
                if target<t:
                    r-=1
                elif target>t:
                    l+=1
                else:
                    return t
        return c
