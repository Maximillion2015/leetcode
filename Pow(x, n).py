import time
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        elif n > 0:
            return self.myPowHelp(x, n)
        else:
            return 1 / self.myPowHelp(x, -n)

    def myPowHelp(self, x, n):
        if n == 1:
            return x
        elif n % 2 == 0:
            return self.myPowHelp(x * x, n // 2)
        else:
            return x * self.myPowHelp(x * x, n // 2)

if __name__ == '__main__':
    time1 = time.time()
    solution = Solution()
    print(solution.myPow(0.00001, 2147483647))
    time2 = time.time()
    print(time2-time1)
