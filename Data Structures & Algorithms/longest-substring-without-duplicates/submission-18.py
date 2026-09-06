class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currentSet = set()
        res = 0
        p1, p2 = 0, 0

        while p2 < len(s):
            if s[p2] in currentSet:
                while s[p2] in currentSet:
                    currentSet.remove(s[p1])
                    p1+=1
            
            currentSet.add(s[p2])
            p2 += 1
            res = max(res, len(currentSet))
                
        return res
        