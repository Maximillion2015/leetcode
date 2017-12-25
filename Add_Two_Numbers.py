from Date_Struct import ListNode

class Solution:
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        r = (l1.val + l2.val) // 10
        l3 = ListNode((l1.val + l2.val) % 10)
        index = l3
        while l1.next != None and l2.next != None:
            node = ListNode((l1.next.val + l2.next.val + r) % 10)
            r = (l1.next.val + l2.next.val + r) // 10
            index.next = node
            l1 = l1.next
            l2 = l2.next
            index = index.next

        if l1.next != None:
            l1.next.val = l1.next.val + r
            index.next = self.addTwoNumbers(l1.next, l2.next)
        elif l2.next != None:
            l2.next.val = l2.next.val + r
            index.next = self.addTwoNumbers(l1, l2)
        elif r == 1:
            index.next = ListNode(1)
            return l3
        else:
            return l3

    def addTwoNumbers(self, l1, l2):
        num1, num2 = self.listToStr(l1), self.listToStr(l2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        sum = int(num1) + int(num2)
        return self.numToList(str(sum)[::-1])

    def numToList(self, strNum):
        l = ListNode(0)
        index = l
        for s in strNum:
            index.next = ListNode(int(s))
            index = index.next
        return l.next


    def listToStr(self, l):
        s = str(l.val)
        while l.next!= None:
            s = s + str(l.next.val)
            l = l.next
        return s

if __name__ == '__main__':
    l1 = ListNode(0)
    l12 = ListNode(8)
    l13 = ListNode(6)
    l1.next = l12
    l12.next = l13

    l2 = ListNode(6)
    l22 = ListNode(7)
    l23 = ListNode(8)
    l2.next = l22
    l22.next = l23

    solution = Solution()
    l3 = solution.addTwoNumbers(l1, l2)
    print(l3)





