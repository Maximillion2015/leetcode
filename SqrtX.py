class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0

        left, right = 0, x
        while left <= right:
            half = (left+right)//2
            if pow(half, 2) == x or (pow(half, 2) < x and pow(half+1, 2) > x):
                result = half
                break
            elif pow(half, 2) > x:
                right = half - 1
            else:
                left = half + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    x = 3
    print(solution.mySqrt(x))
