class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        self.visitedIslands = [[0]*cols for _  in range(rows)]
        self.maxArea = 0
     
        def bfs(grid, i, j):
            q = deque()
            checks = ((1,0), (-1,0), (0,-1) , (0,1))
            q.append((i,j))
            self.visitedIslands[i][j] = -1
            self.curr = 1
            
            while q:
                x0,y0 = q.popleft()
                
                for x,y in checks:
                    cx, cy = x0 + x, y0 + y
                    if 0 <= cx < rows and 0 <= cy < cols:
                        if grid[cx][cy] == 1 and self.visitedIslands[cx][cy] != -1:
                            self.curr += 1
                            self.visitedIslands[cx][cy] = -1
                            q.append((cx,cy))
        
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and self.visitedIslands[r][c] != -1:
                    bfs(grid, r, c)
                    self.maxArea = max(self.maxArea, self.curr)
                else:
                    continue
        return self.maxArea
    
