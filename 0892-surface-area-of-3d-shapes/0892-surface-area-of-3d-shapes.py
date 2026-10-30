class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    ans += 2 + 4 * grid[i][j]

                    if i > 0:
                        ans -= 2 * min(grid[i][j], grid[i-1][j])

                    if j > 0:
                        ans -= 2 * min(grid[i][j], grid[i][j-1])

        return ans