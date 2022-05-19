
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <=1:
            return x
        x_n = 0.3 * x 
        diff = 1
        while diff > 0.1:
            next_x = (0.5 * (x_n + x/x_n))
            diff = abs(x_n - next_x)
            x_n = next_x
        return int(x_n)
            
                
        