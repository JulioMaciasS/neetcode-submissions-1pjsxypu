class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        prefix = [1] * len(nums)
        running_prod = 1
        for i in range(len(nums)):
            prefix[i] = running_prod
            running_prod *= nums[i]

        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= suffix_prod
            suffix_prod *= nums[i]
        return prefix