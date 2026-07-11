class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        We can solve this using a hashmap. Have two variables for tracking. One to just traverse
        through the array, the other to maintain the position of the next element to replace (k).
        We return k in the end.
        """
        k = 0
        m = set()
        for i in range(len(nums)):
            if nums[i] in m:
                continue
            m.add(nums[i])
            nums[k] = nums[i]
            k += 1
        
        return k
        # TC: O(N), SC: O(1)