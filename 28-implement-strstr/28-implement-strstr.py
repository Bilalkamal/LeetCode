class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_length = len(needle)
        for i, l in enumerate(haystack):
            if l == needle[0] and len(haystack[i:]) >= n_length:
                if haystack[i:i+n_length] == needle:
                    return i
        return -1
                
                    
                    
        