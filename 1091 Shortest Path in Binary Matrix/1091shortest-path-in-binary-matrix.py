class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        dir=[(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
        q=deque()
        v=[[0]*n for _ in range(n)]
        q.append((0,0,1))
        v[0][0]=1
        while q:
            x,y,z=q.popleft()
            if x==n-1 and y==n-1:
                return z
            for dx,dy in dir:
                ni=dx+x
                nj=dy+y
                if 0<=ni<n and 0<=nj<n and grid[ni][nj]==0 and v[ni][nj]==0:
                    v[ni][nj]=1
                    q.append((ni,nj,z+1))
        return -1
        