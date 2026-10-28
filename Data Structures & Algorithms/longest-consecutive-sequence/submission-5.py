# LONGEST CONSECUTIVE SEQUENCE


class Solution:
    def attempt1(self, nums):  # O(nlogn) | 52ms 19MB | sorting the array makes it solvable but increase time complexity.

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

    def attempt2(self, nums: list[int]) -> int:  # O(n) O(n) | 45ms 22MB
        """
        - create unique nums
        - iterate over nums to identify start of sequence, i.e. num-1
        - for each start of sequence, find the longest sequence.
        """
        longestSeq = 0
        uniqueNums = set(nums)

        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                seq = 1
                while num + seq in uniqueNums:
                    seq += 1
                longestSeq = max(seq, longestSeq)

        return longestSeq

    def longestConsecutive(self, nums: list[int]) -> int:
        return self.attempt2(nums)


# print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
# print(Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5]), 4)
# print(Solution().longestConsecutive([]), 0)
# print(Solution().longestConsecutive([0]), 1)
# print(Solution().longestConsecutive([0, 0]), 1)


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
print(Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5]), 4)
print(Solution().longestConsecutive([]), 0)
print(Solution().longestConsecutive([0]), 1)
print(Solution().longestConsecutive([0, 0]), 1)