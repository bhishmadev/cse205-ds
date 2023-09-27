class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        x=0
        for x in range(len(s)):
            if s[x] != "*":
                stack.append(s[x])
            else:
                stack.pop()
        return "".join(stack)    