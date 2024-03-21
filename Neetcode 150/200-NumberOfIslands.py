import collections
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r: int, c: int):  # iterative implemented with help of a queue
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            # all possible directions - vertical and horizontal
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r1, c1 = row + dr, col + dc
                    if (r1 in range(rows) and
                            c1 in range(cols) and
                            (r1, c1) not in visited and
                            grid[r1][c1] == "1"):
                        visited.add((r1, c1))
                        q.append((r1, c1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    visited.add((r, c))
                    islands += 1
                    print(visited)

        return islands
