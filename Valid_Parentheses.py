class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        d = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in d.keys():
                l.append(i)
            elif i in d.values() and len(l) != 0 and d.get(l[-1]) == i:
                l.pop()
            else:
                return False
        return len(l) == 0

if __name__ == '__main__':
    solution = Solution()
    s = '[]{'
    print(solution.isValid(s))
