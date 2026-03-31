class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        numsSet = sorted(set(nums)) 
        print(numsSet)
        currentLongest = 1
        currentWindowLength = 1
        p1 = 0
        p2 = 1
        while p1 < p2 and p2 < len(numsSet):
            if numsSet[p2] - numsSet[p1] == 1:
                currentWindowLength += 1
                p1 +=1
                p2 += 1
            else:
                if currentLongest < currentWindowLength:
                    print("Updating currentLongest to: ", currentWindowLength)
                    print("Current pointers: p1-",p1," p2-",p2)
                    currentLongest = currentWindowLength
                currentWindowLength = 1
                p1 = p2
                p2 += 1
       
        if currentLongest < currentWindowLength:
            currentLongest = currentWindowLength
        
        return currentLongest

