# I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''

        while num != 0:
            if num // 1000 != 0:
                temp = num // 1000
                x = 'M'
                result = result + self.intToRomanHelper(temp, x)
                num = num % 1000
            elif num // 100 != 0:
                temp = num // 100
                x, y, z = 'C', 'D', 'M'
                result = result + self.intToRomanHelper(temp, x, y, z)
                num = num % 100
            elif num // 10 != 0:
                temp = num // 10
                x, y, z = 'X', 'L', 'C'
                result = result + self.intToRomanHelper(temp, x, y, z)
                num = num % 10
            else:
                x, y, z = 'I', 'V', 'X'
                result = result + self.intToRomanHelper(num, x, y, z)
                num = 0

        return result

    def intToRomanHelper(self, r, x='', y='', z=''):
        a = {1: x, 2: x + x, 3: x + x + x, 4: x + y, 5: y, 6: y + x, 7: y + x + x, 8: y + x + x + x, 9: x + z}

        return a[r]

if __name__ == '__main__':
    solution = Solution()
    num = 8
    print(solution.intToRoman(num))