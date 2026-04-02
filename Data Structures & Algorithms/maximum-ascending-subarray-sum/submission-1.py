class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        curr = 0
        
        

        # [10,20,30,5,10,50]
        # 65
        for i, num in enumerate(nums):
            
            if nums[i-1] >= num:
                maxSum = max(curr, maxSum)
                curr = num
            else:
                curr += num
        maxSum = max(curr, maxSum)
        return maxSum
            