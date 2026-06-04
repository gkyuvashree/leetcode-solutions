class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n=len(points)
        dia={}
        for i in range(n):
            x,y=points[i]
            for j in range(i+1,n):
                x1,y1=points[j]
                mx=x+x1
                my=y+y1
                d=(x-x1)*(x-x1)+(y-y1)*(y-y1)
                key=(mx,my,d)
                if key not in dia:
                    dia[key]=[]
                dia[key].append((i,j))
        ans=float('inf')
        for pair in dia.values():
            m=len(pair)
            for i in range(m):
                p1,p2=pair[i]
                x1,y1=points[p1]
                for j in range(i+1,m):
                    p2,p3=pair[j]
                    x3,y3=points[p2]
                    x4,y4=points[p3]
                    s1=((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))**0.5
                    s2=((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4))**0.5
                    area=s1*s2
                    ans=min(area,ans)

        if ans==float('inf'):
            return 0
        else:
            return ans