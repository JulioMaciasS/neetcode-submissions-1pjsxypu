class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        currentSet = set()
        longest = 0
        p1=0

        for p2 in range(len(s)):
            while s[p2] in currentSet:
                currentSet.remove(s[p1])
                p1+=1
            currentSet.add(s[p2])
            longest = max(longest, p2-p1+1)
        
        return longest

                