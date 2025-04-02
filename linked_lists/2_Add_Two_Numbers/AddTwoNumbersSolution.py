# Definition for singly-linked list.
from ..utils import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        resultListHead = None
        currentDigitP = None
        l1p = l1
        l2p = l2
        while l1p or l2p or carry:
            l1pVal = l1p.val if l1p else 0
            l2pVal = l2p.val if l2p else 0
            currentDigit = (carry + l1pVal + l2pVal)%10
            carry = (carry + l1pVal + l2pVal)//10
            if not resultListHead:
                resultListHead = ListNode(currentDigit)
                currentDigitP = resultListHead
            else:
                currentDigitP.next = ListNode(currentDigit)
                currentDigitP = currentDigitP.next
            if l1p:
                l1p = l1p.next

            if l2p:
                l2p = l2p.next
        return resultListHead