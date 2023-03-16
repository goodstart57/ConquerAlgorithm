class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        for l in grid: print(l)
            
        skyline_col = [0 for _ in range(n)]
        for y in range(n):
            skyline_col[y] = max(grid[y])
            result -= sum(grid[y])
        print()
        print(skyline_col)
        
        skyline_row = [0 for _ in range(n)]
        for x in range(n):
            row = [0 for _ in range(n)]
            for y in range(n):
                # print(f"({x},{y}) {grid[y][x]}")
                row[y] = grid[y][x]
            skyline_row[x] = max(row)
        print(skyline_row)
        
        for x in range(n):
            for y in range(n):
                result += min(skyline_col[y], skyline_row[x])
        return result