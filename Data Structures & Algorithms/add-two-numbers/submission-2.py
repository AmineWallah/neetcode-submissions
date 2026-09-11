class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Keep going as long as there is a node in l1, l2, or a leftover carry digit
        while l1 or l2 or carry:
            # Get the values, or 0 if we've reached the end of one list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the column sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create the new node with the single digit (total % 10)
            current.next = ListNode(total % 10)
            
            # Move our pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next