"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        current = l3
        carry = 0

        while l1 or l2 or carry:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            carry, sum1 = divmod(x1 + x2 + carry, 10)

            current.next = ListNode(sum1 % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        # print()
        # current3 =l3.next
        # while current3:
        #     print(' -> {0}'.format(current3.val), end='')
        #     current3 = current3.next

        return l3.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(8)

    # current1 = l1
    #     # while current1:
    #     #     print(' -> {0}'.format(current1.val), end='')
    #     #     current1 = current1.next
    #     #
    #     # print()

    l2 = ListNode(0)

    # current2 = l2
    # while current2:
    #     print(' -> {0}'.format(current2.val), end='')
    #     current2 = current2.nexts

    Solution().addTwoNumbers(l1, l2)
