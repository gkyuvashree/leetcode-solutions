class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])

        q = deque()

        v = [[-1] * c for _ in range(r)]

        # put all 0s into queue
        for i in range(r):
            for j in range(c):

                if mat[i][j] == 0:

                    q.append((i, j))

                    v[i][j] = 0

        dir = [(0,1), (1,0), (-1,0), (0,-1)]

        while q:

            x, y = q.popleft()

            for dx, dy in dir:

                a = x + dx
                b = y + dy

                if (0 <= a < r and
                    0 <= b < c and
                    v[a][b] == -1):

                    v[a][b] = v[x][y] + 1

                    q.append((a, b))

        return v