class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False
        
        stack = []
        p = 0

        while p < len(s):
            if s[p] == '{' or s[p] == '[' or s[p] == '(':
                stack.append(s[p])
                p+=1

            elif s[p] == '}' or s[p] == ']' or s[p] == ')':
                if len(stack) == 0:
                    return False
                if s[p] == '}' and stack[-1] == '{':
                    stack.pop()
                    p+=1
                elif s[p] == ']' and stack[-1] == '[':
                    stack.pop()
                    p+=1
                elif s[p] == ')' and stack[-1] == '(':
                    stack.pop()
                    p+=1
                else:
                    return False
        return len(stack) == 0
            
