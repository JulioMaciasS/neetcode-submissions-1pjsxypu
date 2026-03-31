class Solution:
    def isPalindrome(self, s: str) -> bool:

        stack = []
        
        for c in s:
            if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9':
                stack.append(c.lower())
            else:
                continue
        
        initialString = ""
        for i in range(0, len(stack)):
            initialString+=stack[i]

        if initialString == initialString[::-1]:
            return True
        else:
            return False
