class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        
        while l1 or l2 or carry:
            digit1 = 0
            digit2 = 0

            if l1:
                digit1 = l1.val
                l1 = l1.next
            if l2:
                digit2 = l2.val
                l2 = l2.next

            total = digit1 + digit2 + carry

            carry = total // 10
            total = total % 10
            tail.next = ListNode(total)
            tail = tail.next

        return dummy.next
 