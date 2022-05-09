class Solution:
    def findMedianSortedArrays(self, s: List[int], nums2: List[int]) -> float:
        s.extend(nums2)
        s.sort()
        n = len(s)
        return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None
