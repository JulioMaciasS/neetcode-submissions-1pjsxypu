class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1
        currentSet = set()

        p1=0
        p2=1
        currentSet.add(s[0])
        while p2 < len(s):
            if s[p2] not in currentSet:
                currentSet.add(s[p2])
                if p2-p1 + 1 > longest:
                    longest = p2-p1 + 1
                p2+=1
            else:
                while s[p2] in currentSet:
                    currentSet.remove(s[p1])
                    p1+=1
                currentSet.add(s[p2])
                if p2-p1 + 1 > longest:
                    longest = p2-p1 + 1
                p2+=1
    
        return longest
                