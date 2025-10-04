class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python does not have max heap, so we have to change the array
        # to its negative values so that the highest weight in value is in
        # the start of the array
        stones = [-s for s in stones]

        # Min heap the array
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # Say this gives -8
            second = heapq.heappop(stones) # And this give -7

            if first != second: # first is heavier than second, or with negative, second > first
                heapq.heappush(stones, first - second) # -8 - -7 = -1 (it stays negative, which is what we want)
            
        stones.append(0) # In the edge case that there are no stones remaining, just push a 0
        return abs(stones[0]) # So we can return absolute value of stones[0]

# TC: O(n log n)
# SC: O(1)