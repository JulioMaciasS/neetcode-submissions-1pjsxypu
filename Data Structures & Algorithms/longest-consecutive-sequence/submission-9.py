class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        numsSet = sorted(set(nums)) 
        currentLongest = 1

        for num in nums:
            if num-1 in numsSet:
                continue
            else:
                i=1
                length = 1
                while num+i in numsSet:
                    length +=1
                    i+=1
                
                if length > currentLongest:
                    currentLongest = length
        return currentLongest

