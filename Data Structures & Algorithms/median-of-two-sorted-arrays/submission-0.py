class Solution:
    # Define the function taking two sorted arrays and returning a float (the median)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        # Ensure nums1 is always the smaller array to guarantee O(log(min(m,n))) time complexity
        if len(nums1) > len(nums2):
            # If nums1 is larger, swap the arrays by recursively calling the function with flipped arguments
            return self.findMedianSortedArrays(nums2, nums1)

        # Store the length of the smaller array in variable 'x'
        x = len(nums1)
        # Store the length of the larger array in variable 'y'
        y = len(nums2)

        # Initialize the left pointer for binary search at the start of the smaller array
        low = 0
        # Initialize the right pointer for binary search at the end of the smaller array
        high = x

        # Loop until the binary search pointers meet or cross (we are guaranteed to find a valid partition inside)
        while low <= high:
            
            # Calculate the partition index for nums1 (the midpoint of our current search space)
            partitionX = (low + high) // 2
            
            # Calculate the partition index for nums2 so the total elements on the left equal half of both arrays combined
            partitionY = (x + y + 1) // 2 - partitionX

            # Get the largest value on the left side of nums1; use negative infinity if the partition is at index 0 (empty left side)
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            
            # Get the smallest value on the right side of nums1; use positive infinity if partition is at the end (empty right side)
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            # Get the largest value on the left side of nums2; use negative infinity if the partition is at index 0 (empty left side)
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            
            # Get the smallest value on the right side of nums2; use positive infinity if partition is at the end (empty right side)
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Verify if the current partition is valid: left side of nums1 <= right side of nums2 AND left side of nums2 <= right side of nums1
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                
                # Check if the total combined length of both arrays is an even number
                if (x + y) % 2 == 0:
                    # For even lengths, the median is the average of the largest left-side value and the smallest right-side value
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                
                # Otherwise, the total combined length is an odd number
                else:
                    # For odd lengths, the median is simply the largest value on the left side (since the left side holds the extra element)
                    return float(max(maxLeftX, maxLeftY))
            
            # If the partition is invalid because a left-side value in nums1 is strictly greater than a right-side value in nums2
            elif maxLeftX > minRightY:
                # Our partition in nums1 is too far right; move the search space to the left by updating the 'high' pointer
                high = partitionX - 1
            
            # If the partition is invalid because a left-side value in nums2 is strictly greater than a right-side value in nums1
            else:
                # Our partition in nums1 is too far left; move the search space to the right by updating the 'low' pointer
                low = partitionX + 1
