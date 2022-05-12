class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows > len(s) or numRows ==1:
            return s
        lists = [[] for i in range(numRows)]
        diff = -1
        index = 0
        for  l in s:
            if index % (numRows-1) == 0:
                diff *= -1
            lists[index].append(l)
            index += diff
        lists = ["".join(lists[x]) for x in range(numRows)]
        return "".join(lists)
            
        
        