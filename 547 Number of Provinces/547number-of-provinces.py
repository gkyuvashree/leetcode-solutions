class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        g=isConnected
        n=len(g)
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        for i in range(n):
            for j in range(n):
                if g[i][j]==1:
                    a=find(i)
                    b=find(j)
                    if a!=b:
                        parent[a]=b
        return len(set(find(i) for i in range(n)))