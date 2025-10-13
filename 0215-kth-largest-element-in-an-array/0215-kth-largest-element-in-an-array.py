class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]

        # One line python solution
        # return heapq.nlargest(k, nums)[-1]

# TC: O(n log k)
# SC: O(k)