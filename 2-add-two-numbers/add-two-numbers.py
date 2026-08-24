class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            if l1 is not None:
                x = l1.val
            else:
                x = 0

            if l2 is not None:
                y = l2.val
            else:
                y = 0

            total = x + y + carry

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return dummy.next