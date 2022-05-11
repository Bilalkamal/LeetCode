class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for item in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
        