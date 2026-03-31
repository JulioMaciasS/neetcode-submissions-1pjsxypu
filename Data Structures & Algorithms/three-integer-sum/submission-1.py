class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        triplets = []

        for i, n in enumerate(sortedNums):
            if i > 0 and n == sortedNums[i-1]:
                continue
            p1 = i+1
            p2 = len(sortedNums)-1
            while p1 < p2:
                total = n + sortedNums[p1] + sortedNums[p2]
                if total == 0:
                    triplets.append([n,sortedNums[p1],sortedNums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and sortedNums[p1] == sortedNums[p1 - 1]:
                            p1 += 1
                    while p1 < p2 and sortedNums[p2] == sortedNums[p2 + 1]:
                            p2 -= 1

                elif total > 0:
                    p2 -= 1
                else:
                    p1 += 1
                    
        return triplets

