"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        result = ListNode(0)
        tail = result
        while l1 or l2:
            if not l2 or (l1 and l1.val < l2.val):
                tail.next = ListNode(l1.val)
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                tail = tail.next
                l2 = l2.next

        return result.next


if __name__ == '__main__':
    s1 = Solution()

    l1 = ListNode(x=1)
    l1.next = ListNode(x=2)
    l1.next.next = ListNode(x=4)

    l2 = ListNode(x=1)
    l2.next = ListNode(x=3)
    l2.next.next = ListNode(x=4)

    res = s1.mergeTwoLists(l1, l2)

    while res:
        print(res.val)
        res = res.next
