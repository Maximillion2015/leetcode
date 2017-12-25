# I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        result = 0

        size = len(s)

        while size > 1:
            if d.get(s[size-1]) <= d.get(s[size-2]):
                result = result + d.get(s[size-1])
                size = size - 1
            else:
                result = result + d.get(s[size-1]) - d.get((s[size-2]))
                size = size - 2

        if size == 1:
            result = result + d.get(s[0])

        return result

if __name__ == '__main__':
    solution = Solution()
    s = 'DCXXI'
    print(solution.romanToInt(s))