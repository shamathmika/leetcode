class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subst = set() # Use this to maintain the longest substring

        l = 0
        max_ = 0 # Length of longest substring

        for r in range(len(s)):
            while s[r] in subst: # Remove the character until the repeated character is gone
                subst.remove(s[l])
                l += 1 # Increase left pointer
            subst.add(s[r])
            max_ = max(max_, len(subst))

        return max_

# TC: O(n)
# SC: O(n)