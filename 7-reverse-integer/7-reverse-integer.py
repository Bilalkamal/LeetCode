class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x<0:
            negative = True 
        if negative:
            x = str(x)[1:]
        x = str(x)[::-1]
        x = int(x)
        if -2**31 >x or x>(2**31) -1:
            return 0
        return x*-1 if negative else x
        
        