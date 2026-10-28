class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # through O N space.

        nums3 = []

        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
            elif i < m:
                nums3.extend(nums1[i:])
                break
            elif j < n:
                nums3.extend(nums2[j:])
                break

        # print(nums3)
        mid = (m + n) // 2
        if (m + n) % 2 == 0:
            return (nums3[mid] + nums3[mid - 1]) / 2
        else:
            return float(nums3[mid])
