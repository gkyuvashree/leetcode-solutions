class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)

        while l <= r:
            mid = l + (r - l) // 2
            curr = 0
            for n in nums:
                if n >= mid:
                    curr += 1
            
            if (curr > mid):
                l = mid + 1
            elif (curr < mid):
                r = mid - 1
            else:
                return mid
        
        return - 1
        