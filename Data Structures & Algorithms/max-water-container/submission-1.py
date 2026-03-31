class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestVolume = 0

        p1 = 0
        p2 = len(heights) - 1
        windowSize = len(heights)
        
        while windowSize >= 2:
            while p2 < len(heights):
                currentVolume = min(heights[p1], heights[p2]) * (p2 - p1)

                if currentVolume > largestVolume:
                    largestVolume = currentVolume
                p1 += 1
                p2 += 1

            windowSize -= 1
            p2 = windowSize - 1
            p1 = 0

        return largestVolume