class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + num
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])

                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

        return res
