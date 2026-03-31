class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        minVal = 1000
        while l<=r:
            mid = l + (r - l) // 2
            minVal = min(minVal, nums[mid])

            if nums[mid] < nums[r]:
                r = mid-1
            else:
                l = mid + 1
        return minVal