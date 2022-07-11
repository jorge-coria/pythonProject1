# Create ListNode that points to 1st LL node, and tail.next points to last LL node(s)
# Time + Memory Complexity: O(m + n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


l1 = createLinkedList([2, 4, 6])
l2 = createLinkedList([1, 3, 5, 8, 10])

print(toList(Solution.mergeTwoLists(l1, l2)))