class Solution:
    def findMin(self, nums: List[int]) -> int:
        currentMin = 1000
        for num in nums:
            currentMin = min(num,currentMin)
        return currentMin