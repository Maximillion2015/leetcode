from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = 0, 0
        while index1 < m and index2 < n:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                nums1[index1+1:] = nums1[index1:len(nums1)-1]
                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1
                m += 1
        if index2 < n:
            nums1[index1:] = nums2[index2:]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    nums2 = [1, 2, 2]
    m = 6
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)
