class Solution:

    def attempt1(self, nums, target):
        """considering that nums are sorted. 
        it means LEFT is lesser than RIGHT (or RIGHT is lesser than LEFT).

        1 2 3 4 , target = 4
        l=1 r=4 => 5 > target so decrease RIGHT.
        l=1 r=3 => 4. OK.
        """
        l=0
        r=len(nums)-1
        while l<r:
            sum_value = nums[l]+nums[r]
            if sum_value == target:
                return [l+1, r+1]
            elif sum_value < target:
                l += 1
            else:
                r -= 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.attempt1(numbers, target)