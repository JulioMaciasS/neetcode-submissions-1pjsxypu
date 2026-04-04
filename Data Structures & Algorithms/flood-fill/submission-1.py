class Solution:
    """
    Input parameters:
    - 2d Array with image pixels
    - sr, sc (x y cordintanes to start from)
    - color: color to replace the pixels with

    Task:
    Replace the horizontal and vertical adjacent pixels if they match the color of the starting pixels

    Solution:
    Use iterative BFS to iterate through the pixels.

    Edge cases:
    The array length is 0
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []

        # current adjacent pixels that get added during the check
        x, y = sr, sc
        rows, cols = len(image), len(image[0])
        startingColor = image[x][y]
        image[x][y] = color

        if startingColor == color:
            return image

        q = deque()

        q.append((x,y))
        checks = ((-1,0),(1,0),(0,-1),(0,1))
        while q:
            # BFS Implementation
            x0, y0 = q.popleft()
            for x,y in checks:
                currentX = x0 + x
                currentY = y0 + y

                if 0 <= currentX < rows and 0 <= currentY < cols:
                    if image[currentX][currentY] == startingColor:
                        q.append((currentX, currentY))
                        image[currentX][currentY] = color
        return image
                    
