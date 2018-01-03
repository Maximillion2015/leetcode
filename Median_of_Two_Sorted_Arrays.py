class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1, len2 = len(nums1), len(nums2)

        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1

        if len2 == 0:
            raise ValueError

        # i表示排序完成后第一行有i个元素在左边，j表示排序完成后第一行有j个元素在左边
        iMin, iMax, half_length, i, j = 0, len1, (len1 + len2 + 1) // 2, 0, 0

        # 二分查找，找到i和j的值
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = half_length - i

            if i < len1 and nums2[j-1] > nums1[i]:
                iMin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                iMax = i - 1
            else:
                break


        if i == 0: left_max = nums2[j-1]
        elif j == 0: left_max = nums1[i-1]
        else: left_max = max(nums1[i-1], nums2[j-1])

        if (len1 + len2) % 2 != 0:
            return float(left_max)
        else:
            if i == len1:
                right_min = nums2[j]
            elif j == len2:
                right_min = nums1[i]
            else:
                right_min = min(nums1[i], nums2[j])

            return (left_max + right_min) / 2




if __name__ == '__main__':
    solution = Solution()
    nums1 = [4,5]
    nums2 = [1, 3]
    print(solution.findMedianSortedArrays(nums1, nums2))