import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0

        while heap:
            max_node, x, y = heapq.heappop(heap)
            result = max(result, max_node)
            if x == n - 1 and y == n - 1:
                return result
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    heapq.heappush(heap, (grid[ny][nx], nx, ny))
                    visited.add((nx, ny))
        return result

"""
class Solution:
    def dfs(self, x, y, visited, result, max_node):
        visited[y][x] = 1
        max_node = max(self.grid[y][x], max_node)
        # print(f"({x},{y}) visit")
        # print(f"  max node {max_node} / result {result}")
        # print(f"  visited {visited}")
        if visited[y][x] > result:
            pass
        elif (x, y) == (self.n - 1, self.n - 1):
            # print(f"    result {result} / max_node {max_node}")
            result = min(result, max_node)
        else:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= x + dx < self.n and 0 <= y + dy < self.n and not visited[y+dy][x+dx]:
                    # print(f"  next node ({x+dx}, {y+dy})")
                    result = self.dfs(x+dx, y+dy, visited, result, max_node)
                    visited[y+dy][x+dx] = 0
                    # print(f"  visited {visited} unvisited node ({x+dx}, {y+dy})")
        return result
        
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.grid, self.n = grid, len(grid)
        result = self.n*self.n
        
        visited = [[0 for _ in range(self.n)] for __ in range(self.n)]
        
        return self.dfs(0, 0, visited, result, 0)
"""