class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        length = len(nums)
        for r in range(1, length):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1
        return l
            
                
            