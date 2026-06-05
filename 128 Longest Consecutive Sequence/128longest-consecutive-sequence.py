class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for i in s:
            if i-1 not in s:
                current=i
                l=1
                while current+1 in s:
                    current+=1
                    l+=1
                longest=max(l,longest)
        return longest