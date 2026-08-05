class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        water=0
        for right in range(len(height)):
            while stack and height[right]>height[stack[-1]]:
                base=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                w=right-left-1
                h=min(height[right],height[left])-height[base]
                water+=w*h
            stack.append(right)
        return water
        