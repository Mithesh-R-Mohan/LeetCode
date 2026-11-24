class Solution:
    def islandPerimeter(self, grid):
        r = len(grid)
        c = len(grid[0])
        p = 0
        for ri in range(r):
            for ci in range(c):
                if grid[ri][ci] == 1:
                    p += 4
                    if ri > 0 and grid[ri - 1][ci] == 1:
                        p -= 2
                    if ci > 0 and grid[ri][ci - 1] == 1:
                        p -= 2
        return p