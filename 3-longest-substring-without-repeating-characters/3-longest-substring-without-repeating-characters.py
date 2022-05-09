class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        length = len(s)
        for i in range(length):
            my_set = set()
            for x in range(i, length):
                if s[x] in my_set:
                    break 
                my_set.add(s[x])
                if len(my_set) > longest:
                    longest = len(my_set)
        return longest