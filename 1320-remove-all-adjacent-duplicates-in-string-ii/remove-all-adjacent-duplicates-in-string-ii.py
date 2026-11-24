class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[] # store [char,count]
        for char in s:
            if not stack or stack[-1][0]!=char:
                stack.append([char,1])
            else:
                count=stack[-1][1]+1
                if(count<k):
                    stack.append([char,count])
                else:
                    pops=k-1
                    while pops:
                        stack.pop()
                        pops-=1
        
        return "".join(item[0] for item in stack)

        # stack = []  # Stores pairs of [char, count]
        # for char in s:
        #     # If the current char matches the top of the stack, increment its count
        #     if stack and stack[-1][0] == char:
        #         stack[-1][1] += 1
                
        #         # If we hit k consecutive duplicates, remove the whole group in O(1)
        #         if stack[-1][1] == k:
        #             stack.pop()
        #     else:
        #         # Otherwise, push a new character with a count of 1
        #         stack.append([char, 1])
                
        # # Rebuild the final string by multiplying each char by its remaining count
        # return "".join(char * count for char, count in stack)

                
        