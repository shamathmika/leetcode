class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Calculate current area between the two pointers and move the one with smaller height
        l, r = 0, len(height) - 1
        most = 0

        while r > l:
            current = (r - l) * min(height[l], height[r])
            
            if current > most:
                most = current
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return most

# TC: O(n)
# SC: O(1)