class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        left=0
        for right in range(left,len(nums)):
            if nums[left]!=nums[right]:
                left+=1
                nums[left]=nums[right]
        return left+1