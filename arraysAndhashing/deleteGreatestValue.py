class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        res = 0
        cols = len(grid[0])
        for i in range(cols - 1, -1, -1):
            maxVal = 0
            for row in grid:
                maxVal = max(maxVal, row[i])
            res += maxVal
        return res