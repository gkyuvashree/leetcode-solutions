class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            roota=find(a)
            rootb=find(b)
            if roota==rootb:
                return False
            parent[roota]=rootb
            return True
        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                cost=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((cost,i,j))
        edges.sort()
        ans=0
        for cost,a,b in edges:
            if union(a,b):
                ans+=cost
        return ans