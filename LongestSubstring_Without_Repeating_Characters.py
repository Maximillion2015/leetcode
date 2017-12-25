class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        left, right = 0, 1
        maxLen = 0
        while right <= l:
            strSet = set(s[left:right])
            if len(strSet) == (right - left):
                maxLen = max(maxLen, (right - left))
            else:
                while left < right:
                    if s[left] == s[right-1]:
                        left = left + 1
                        break
                    left = left + 1
            right = right + 1
        return maxLen

if __name__ == '__main__':
    solution = Solution()
    s = ''
    print(solution.lengthOfLongestSubstring(s))
