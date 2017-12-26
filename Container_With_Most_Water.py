class Solution:
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        result = 0
        i = 0
        for i in range(len(height)):
            j = i + 1
            while j < len(height):
                result = max(result, (j-i)*min(height[i], height[j]))
                j = j + 1
        return result

    def maxArea(self, height):
        left, right = 0, len(height)-1
        result = 0
        # 由于一条较低的边高度固定了，因此宽度最长的情况肯定是包含该边的结果中容量最大的。
        while left < right:
            if height[left] < height[right]:
                result = max(result, height[left] * (right - left))
                left = left + 1
            else:
                result = max(result, height[right] * (right - left))
                right = right - 1

        return result

if __name__ == '__main__':
    solution = Solution()
    height = [2, 1]
    print(solution.maxArea(height))