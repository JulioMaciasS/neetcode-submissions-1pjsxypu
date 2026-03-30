from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency of each value
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        return sorted_nums[:k]
        