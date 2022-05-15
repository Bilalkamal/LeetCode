class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {"(":")", "{":"}", "[":"]"}
        for p in s:
            if p in pars.keys():
                stack.append(pars[p]) 
            else:
                if not stack:
                    return False
                elif p != stack[-1]:   
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True