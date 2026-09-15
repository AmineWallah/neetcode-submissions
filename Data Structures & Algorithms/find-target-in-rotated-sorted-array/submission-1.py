class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Check if the LEFT half is sorted
            if nums[l] <= nums[m]:
                # Is the target within this strictly sorted left half?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is here, discard right half
                else:
                    l = m + 1  # Target is NOT here, discard left half
            
            # Otherwise, the RIGHT half must be sorted
            else:
                # Is the target within this strictly sorted right half?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is here, discard left half
                else:
                    r = m - 1  # Target is NOT here, discard right half
                    
        return -1