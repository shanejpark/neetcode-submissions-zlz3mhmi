from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        for char in s:
            if char in '([{':
                queue.append(char)
            else:
                if not queue:
                    return False
                popped = queue.pop()
                if char == ')' and popped != '(':
                    return False
                if char == ']' and popped != '[':
                    return False
                if char == '}' and popped != '{':
                    return False
        return len(queue) == 0
                
        