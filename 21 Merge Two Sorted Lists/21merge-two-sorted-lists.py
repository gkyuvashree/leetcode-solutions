# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Tail will always point to the last node in the merged list
        tail = dummy

        # Go through both lists until one of them is empty
        while list1 and list2:
            # Compare values from both lists
            if list1.val < list2.val:
                # Attach the smaller node to the tail
                tail.next = list1
                # Move list1 ahead
                list1 = list1.next
            else:
                # Attach the smaller or equal node to the tail
                tail.next = list2
                # Move list2 ahead
                list2 = list2.next

            # Move the tail to the newly added node
            tail = tail.next

        # If one of the lists is not empty, attach the rest
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # The merged list starts from dummy.next
        return dummy.next
