class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_arr = nums[0]
        current = 0
        for n in nums:
            current = 0 if current < 0 else current
            current += n
            max_arr = max(max_arr, current)
        return max_arr