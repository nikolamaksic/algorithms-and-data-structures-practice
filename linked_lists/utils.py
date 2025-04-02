class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals)
    
    def __eq__(self, other):
        curr = self
        other_curr = other
        while curr and other_curr:
            if curr.val != other_curr.val:
                return False
            curr = curr.next
            other_curr = other_curr.next

        return curr is None and other_curr is None

    __repr__ = __str__

class LinkedList:
    def __init__(self, listOfVal):
        self.head = None
        prevNode = None
        for v in listOfVal:
            newNode = ListNode(v)
            if not self.head:
                self.head = newNode
            if prevNode:
                prevNode.next = newNode
            prevNode = newNode

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)

    def __eq__(self, otherList):
        cl = self.head
        ol = otherList()

        while cl and ol:
            if cl.val != ol.val:
                return False
            cl = cl.next
            ol = ol.next

        if cl or ol:
            return False
        return True


    def __call__(self):
        return self.head