class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s=set()
        for x,y in points:
            s.add((x,y))
        ans=float('inf')
        n=len(points)
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                if x1==x2 or y1==y2:
                    continue
                if (x1,y2) in s and (x2,y1) in s:
                    area=abs(x2-x1)*abs(y2-y1)
                    ans=min(ans,area)
        if ans==float('inf'):
            return 0
        else:
            return ans         

        