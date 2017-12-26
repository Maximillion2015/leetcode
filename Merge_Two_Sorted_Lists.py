# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        index = result

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                index.next = l1
                l1 = l1.next
            else:
                index.next = l2
                l2 = l2.next
            index = index.next

        if l1 == None:
            index.next = l2
        else:
            index.next = l1

        return result.next


