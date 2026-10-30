class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = nums[0]
        for i in range(1, len(nums)):
            sum ^= nums[i]
        return sum