class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestVolume = 0

        p1 = 0
        p2 = len(heights)-1
        
        while p1 < p2:
            currentVolume = min(heights[p1],heights[p2]) * (p2-p1)
            if currentVolume > largestVolume:
                largestVolume = currentVolume
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1+= 1


        return largestVolume
            
            