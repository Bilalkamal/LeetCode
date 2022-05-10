class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        shortest_word = min(strs, key=len)
        for i in range(len(shortest_word)):
            letter = strs[0][i]
            prefix += letter
            for word in strs:
                if word[i] != letter:
                    prefix.pop()
                    return "".join(prefix)


        return "".join(prefix)
        