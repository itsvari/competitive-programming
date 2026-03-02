class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingBrackets = {")": "(", "]": "[", "}": "{"}

        for character in s:
            if character in matchingBrackets:
                if stack and stack[-1] == matchingBrackets[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if (not stack) else False
