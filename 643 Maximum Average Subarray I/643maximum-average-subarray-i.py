class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum=sum(nums[:k])
        wmax=wsum
        for i in range(k,len(nums)):
            wsum+=nums[i]-nums[i-k]
            wmax=max(wmax,wsum)
        return wmax/k