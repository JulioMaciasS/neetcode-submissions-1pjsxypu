class Solution:
    def isPalindrome(self, s: str) -> bool:

        stack = []
        
        for c in s:
            if  'a'<= c <= 'z' or 'A'<= c <= 'Z' or '0'<= c <= '9':
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
