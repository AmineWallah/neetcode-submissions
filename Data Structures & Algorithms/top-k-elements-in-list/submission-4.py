class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        # We build our frequency dictionary

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        maximum = 0
        largest_key = 0
        result = []
        for _ in range(k):
            for key in frequency:
                if frequency[key] > maximum:
                    maximum = frequency[key]
                    largest_key = key
            maximum = 0
            result.append(largest_key)
            frequency.pop(largest_key, None)

        return result
            
