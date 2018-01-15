class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        import sys
        d = sys.maxsize

        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s1 = nums[i] + nums[l+1] + nums[r]
                s2 = nums[i] + nums[l] + nums[r-1]
                s = nums[i] + nums[l] + nums[r]
                if nums[l] == nums[r]:
                    if abs(s - target) < abs(d - target):
                        d = s
                    break

                if abs(s - target) < abs(d - target):
                    d = s


                if abs(s1 - target) > abs(s2 - target):
                    r -= 1
                elif abs(s1 - target) < abs(s2 - target):
                    l += 1
                else:
                    ll, rr = l, r
                    while nums[rr] == nums[rr-1] and rr > ll:
                        rr -= 1
                    while nums[ll] == nums[ll+1] and rr > ll:
                        ll += 1
                    if abs(nums[i] + nums[rr-1] + nums[ll] - target) > abs(nums[i] + nums[rr] + nums[ll+1] - target):
                        l = ll + 1
                    elif abs(nums[i] + nums[rr-1] + nums[ll] - target) < abs(nums[i] + nums[rr] + nums[ll+1] - target):
                        r = rr - 1
                    else:
                        break

        return d


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2]
    # nums = [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
    target = -59
    print(solution.threeSumClosest(nums, target))