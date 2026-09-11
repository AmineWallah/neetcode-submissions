# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''
        while l1:
            str1 += f'{l1.val}'
            l1 = l1.next

        while l2:
            str2 += f'{l2.val}'
            l2 = l2.next

        # flipping strings
        str1 = str1[::-1]
        str2 = str2[::-1]

        res = str(int(str1) + int(str2))
        res = res[::-1]

        dummy = ListNode()
        head = dummy
        for char in res:
            dummy.next = ListNode(int(char))
            dummy = dummy.next

        return head.next


