class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans += 1

        for row in grid:
            ans += max(row)

        for j in range(len(grid[0])):
            maxi = 0
            for i in range(len(grid)):
                maxi = max(maxi, grid[i][j])
            ans += maxi

        return ans