class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    q.append((i, j))
                    while q:
                        qi, qj = q.popleft()
                        for di, dj in directs:
                            ni, nj = di + qi, dj + qj
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1":
                                grid[ni][nj] = "0"
                                q.append((ni, nj))
        
        return num_islands
        