class Solution(object):
    def modifiedList(self, nums, head):
        s = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
