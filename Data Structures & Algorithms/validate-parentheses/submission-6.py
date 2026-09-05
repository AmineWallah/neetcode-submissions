class Solution:
    def isValid(self, s: str) -> bool:
        counterparts = {
            ']': '[',
            ')': '(',
            '}': '{',
        }

        stack = []
        
        for char in s:
            if char not in counterparts:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                thing = stack.pop()
                if counterparts[char] != thing:
                    return False
        
        if len(stack) > 0:
            return False
        return True
