class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if i!=r-1:
                    if grid[i][j]!=grid[i+1][j]:
                        return False
                    
                if j!=c-1:
                    if grid[i][j]==grid[i][j+1]:
                        return False
        return True
        