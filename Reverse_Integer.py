import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        absX = abs(x)
        s = str(absX)[::-1]
        if x >= 0 and int(s) <= 2**31:
        	return int(s)
        elif x < 0 and int(s) <= 2**31-1:
        	return -int(s)
        else:
        	return 0


if __name__ == '__main__':
	solutoin = Solution()
	x = 1563847412
	print(2**31)
	print(solutoin.reverse(x))