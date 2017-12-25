class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '' or None:
            return ''

        l = len(s)
        array = [[0 for x in range(l)] for x in range(l)]
        for i in range(l):
            for j in range(l):
                if s[i] == s[j]:
                    array[i][j] = 1

        i = l - 1
        while i >= 0:
            j = 0
            isPalindrome = True
            while j <= i:
                if array[i-j][j] == 0:
                    isPalindrome = False
                j = j + 1

            if isPalindrome:
                return

            i = i - 1

        return


if __name__ == '__main__':
    solution = Solution()
    s = 'abada'
    print(solution.longestPalindrome(s))