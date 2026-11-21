class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if stack and stack[-1]==char: # if stack non empty hai and current string element equals to current stack element
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

        