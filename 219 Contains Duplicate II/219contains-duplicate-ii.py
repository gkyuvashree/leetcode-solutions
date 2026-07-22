class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ls={}
        for i,num in enumerate(nums):
            if num in ls:
                if (i-ls[num])<=k:
                    return True
            ls[num]=i
        return False