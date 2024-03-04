class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen.get(c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True


s = Solution()
print(s.isValid("{}"))
print(s.isValid("[{}]"))
print(s.isValid("{}]"))
print(s.isValid("({}]"))