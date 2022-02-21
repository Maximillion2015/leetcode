class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        result = list()
        for i in range(n):
            if i == 0:
                result.append(1)
            elif i == 1:
                result.append(2)
            else:
                result.append(result[i-1] + result[i-2])
        return result[n-1]


if __name__ == '__main__':
    solution = Solution()
    n = 0
    print(solution.climbStairs(n))
