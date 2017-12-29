class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        strLen = len(s)
        sIndex, lIndex = 0, 0
        l = [[] for i in range(numRows)]
        tag = True
        while sIndex < strLen:
            l[lIndex].append(s[sIndex])
            sIndex = sIndex + 1
            if tag:
                lIndex = lIndex + 1
            else:
                lIndex = lIndex - 1

            if lIndex == numRows - 1 or lIndex == 0:
                tag = not tag


        result = ''
        for innerL in l:
            result = result + ''.join(innerL)

        return result

if __name__ == '__main__':
    solution = Solution()
    s = 'AB'
    numRows = 1
    print(solution.convert(s, numRows))