# LONGEST CONSECUTIVE SEQUENCE


class Solution:
    def attempt1(self, nums):  # sorting the array would make it easy to solve: buy O(NlogN)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        nums.sort()

        # 1 2 3 4 100 200 => 4
        # 2 3 4 4 5 10 20 => 4
        prv = nums[0]
        seq = 1
        longestSeq = seq
        for num in nums:
            if num == prv:
                continue
            if prv + 1 == num:
                seq += 1
                longestSeq = max(longestSeq, seq)
            else:
                seq = 1
            prv = num

        return longestSeq

    def longestConsecutive(self, nums: list[int]) -> int:
        return self.attempt1(nums)