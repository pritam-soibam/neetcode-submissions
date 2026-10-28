class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorting will increase time complexity to n.logn

        # identify unique nums
        # iterate over it, and identify starting sequence,
        # for each starting sequence, find max.
        if not nums:
            return 0

        maxSeq = 1
        unique = set(nums)
        for num in unique:
            if num - 1 not in unique:
                seq = 1
                while num + seq in unique:
                    seq += 1
                maxSeq = max(maxSeq, seq)

        return maxSeq
