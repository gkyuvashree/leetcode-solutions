class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r = len(grid)
        c = len(grid[0])
        q = deque()
        q.append((0, 0, k, 0))
        v = [[-1] * c for _ in range(r)]
        v[0][0] = k
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y, rem, steps = q.popleft()
            if x == r - 1 and y == c - 1:
                return steps
            for dx, dy in dir:
                ni = x + dx
                nj = y + dy
                if 0 <= ni < r and 0 <= nj < c:
                    nk=rem-grid[ni][nj]
                    if nk>=0 and nk>v[ni][nj]:
                        v[ni][nj]=nk
                        q.append((ni,nj,nk,steps+1))
        return -1