class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        length = len(s) - 1
        for i, c in enumerate(s):
            if i<length and (convert[s[i]] < convert[s[i+1]]):
                sum -= convert[c]
            else:
                sum += convert[c]
        return sum
        