class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        We can solve this using a hashset. Have two variables for tracking. One to just traverse
        through the array, the other to maintain the position of the next element to replace (k).
        We return k in the end. This is the brute force approach where we need extra space.
        We can avoid the hash set completely since the array is in non-decreasing order. So we
        only need to check with the previous element. If not, replace with k else just keep
        traversing
        """
        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            nums[k] = nums[i]
            k += 1
        return k
        # TC: O(N), SC:O(1)

        # # Brute force
        # k = 0
        # m = set()
        # for i in range(len(nums)):
        #     if nums[i] in m:
        #         continue
        #     m.add(nums[i])
        #     nums[k] = nums[i]
        #     k += 1
        
        # return k
        # # TC: O(N), SC: O(N-k)