class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length < 2:
            return length

        index, count = 1, 1

        while count != length:
            if nums[index] == nums[index-1]:
                nums.remove(nums[index])
            else:
                index += 1

            count += 1

        return len(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.removeDuplicates(nums))
    print(nums)