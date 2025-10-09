class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            d = x ** 2 + y ** 2
            heap.append([d, x, y])
        
        heapq.heapify(heap)

        ret = []
        while k > 0:
            d, x, y = heapq.heappop(heap)
            ret.append([x, y])
            k -= 1
        
        return ret

# TC: O(k log n)
# SC: O(n)