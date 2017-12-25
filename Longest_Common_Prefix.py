import sys
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''

        result = strs[0]
        i = 0

        minLength = sys.maxsize
        for str in strs:
            minLength = min(len(str), minLength)
        while i < minLength :
            for str in strs:
                index = str[i]
                if index != result[i]:
                    return result[:i]
            i = i + 1

        return result[:i]



if __name__ == '__main__':
    solution = Solution()
    strs = ['hello', 'hell', 'hesss', 'h', 'ha']
    print(solution.longestCommonPrefix(strs))