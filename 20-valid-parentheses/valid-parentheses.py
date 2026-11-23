class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={"(":")","[":"]","{":"}"}
        stack=[]
        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if not stack or hashmap[stack.pop()]!=char:
                    return False
        return not stack

