class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                l=j+1
                r=n-1
                while l<r:
                    total=nums[i]+nums[j]+nums[l]+nums[r]
                    if total==target:
                        ans.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
                    elif total<target:
                        l+=1
                    else:
                        r-=1
        #conveting tuple into list cuz leetcode wants list only
        result=[]
        for x in ans:
            result.append(list(x))
        return result
        