class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {"(":")", "{":"}", "[":"]"}
        for p in s:
            if p in pars.keys():
                stack.append(pars[p]) 
            else:
#               if stack is empty or the last item is not the similar, return False.
#               otherwise, pop!
                if not stack:
                    return False
                elif p != stack[-1]:   
                    return False
                else:
                    stack.pop()
#       if stack still has some items
        if stack:
            return False
        return True