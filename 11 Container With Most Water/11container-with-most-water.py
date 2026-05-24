class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_water=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            area=h*w
            if area>max_water:
                max_water=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_water
        