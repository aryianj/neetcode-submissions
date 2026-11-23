class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'{':'}', '[':']', '(':')'}
        stack = []

        for c in s:
            if c in valid.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or valid[stack.pop()] != c:
                    return False
        return len(stack) == 0