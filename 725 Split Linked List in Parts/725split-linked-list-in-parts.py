class Solution(object):
    def splitListToParts(self, head, k):
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        n = length // k
        r = length % k
        result, curr = [], head

        for i in range(k):
            part_head = curr
            part_size = n + (1 if i < r else 0)
            for j in range(part_size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            result.append(part_head)

        return result
