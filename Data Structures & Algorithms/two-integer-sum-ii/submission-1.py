class Solution:
    def attempt1(self, nums, target):
        """considering that nums are sorted.
        it means LEFT is lesser than RIGHT (or RIGHT is lesser than LEFT).

        1 2 3 4 , target = 4
        l=1 r=4 => 5 > target so decrease RIGHT.
        l=1 r=3 => 4. OK.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.attempt1(numbers, target)
