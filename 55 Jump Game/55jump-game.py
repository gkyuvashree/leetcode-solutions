class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far=0
        for i in range(len(nums)):
            if i>far:
                return False
            else:
                far=max(far,i+nums[i])
        return True