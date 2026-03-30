
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    #    heap = []
    #    heapq.heapify(heap)
       c = Counter(nums)
       sortedNums = sorted(c, key=c.get, reverse=True)

       return sortedNums[:k]
