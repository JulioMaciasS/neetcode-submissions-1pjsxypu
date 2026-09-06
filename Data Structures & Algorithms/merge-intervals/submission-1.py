class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        mergedArray = []
        currIntevarl = intervals[0]
    
        for interval in intervals[1:]:
            if currIntevarl[1] >= interval[0]:
                currIntevarl[1] = max(currIntevarl[1], interval[1])
            else:
                mergedArray.append(currIntevarl)
                currIntevarl = interval

        mergedArray.append(currIntevarl)

        return mergedArray
            # if the second element of the current array is equal or more 
            # than the first element of the next array, merge into 1
            # do this until this condition does not happen, and 