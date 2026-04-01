class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            directions = [[0,-1],[0,1],[1,0],[-1,0]]
            
            while q:
                r, c = q.popleft()
                

                for dr,dc in directions:
                    currR, currC = r + dr, c + dc
                    if ((currR) in range(rows) and
                        (currC) in range(cols) and
                        grid[currR][currC] == "1" and
                        (currR, currC) not in visit):
                        q.append((currR, currC))
                        visit.add((currR,currC))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands