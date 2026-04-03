class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        return  heapq.heappop(self.minHeap)