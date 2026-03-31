class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for n in nums_set:
            if n-1 in nums_set:
                continue
            else:
                i = 1
                length = 1
                while n + i in nums_set:
                    length += 1
                    i += 1
                if length > longest:
                    longest = length
        return longest

